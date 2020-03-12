import json
import math
import string
from ast import literal_eval
from pathlib import Path

import ftfy
import jsonlines
import plac
import validators
from preshed.counter import PreshCounter
from spacy.lang.en import stop_words as en_stop_words
from spacy.lang.zh import stop_words as zh_stop_words
from tqdm import tqdm


class Word:
    counter = -1

    def __init__(self, word_str, cluster, probs):
        self._word = word_str
        self._cluster = cluster
        self._probs = probs

        chinese_punct = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
        self._punct_list = list(set(string.punctuation + chinese_punct))

        chinese_whitespace = ""
        self._whitespace_list = list(set(string.whitespace + chinese_whitespace))

        english_stopword = en_stop_words.STOP_WORDS
        chinese_stopword = zh_stop_words.STOP_WORDS
        self._stopword_list = {*english_stopword, *chinese_stopword}

        chinese_quote = "“”‘’"
        english_quote = "\"'"
        self._qute_list = list(set(english_quote + chinese_quote))

        chinese_left_punct = "<([{"
        english_left_punct = "＜（［「『【〔〖〘〚｛"
        self._left_punct_list = list(set(english_left_punct + chinese_left_punct))

        chinese_right_punct = ">)]}"
        english_right_punct = "＞）］」』】〕〗〙〛｝"
        self._right_punct_list = list(set(english_right_punct + chinese_right_punct))

    @property
    def orth(self):
        return self._word

    @property
    def id(self):
        self.__class__.counter += 1

        return self.__class__.counter

    @property
    def lower(self):
        return self._word.lower()

    @property
    def norm(self):
        return self._word

    @property
    def shape(self):
        return "".join(map(lambda x: "X" if x.isupper() else "x", self._word))

    @property
    def prefix(self):
        return self._word[0]

    @property
    def suffix(self):
        return self._word[-1]

    @property
    def length(self):
        return len(self._word)

    @property
    def cluster(self):
        return self._cluster

    @property
    def prob(self):
        return self._probs.get(self, 0)

    @property
    def is_alpha(self):
        return self._word.isalpha()

    @property
    def is_ascii(self):
        # only for py 3.7
        # return self._word.isascii()
        try:
            self._word.encode('ascii')
        except UnicodeEncodeError:
            return False

        return True

    @property
    def is_digit(self):
        return self._word.isdigit()

    @property
    def is_lower(self):
        return self._word.islower()

    @property
    def is_punct(self):
        return self._word in self._punct_list

    @property
    def is_space(self):
        return self._word in self._whitespace_list

    @property
    def is_title(self):
        return self._word.istitle()

    @property
    def is_upper(self):
        return self._word.isupper()

    @property
    def like_url(self):
        return bool(validators.url(self._word))

    @property
    def like_num(self):
        # TODO(howl-anderson): fix it later
        return False

    @property
    def like_email(self):
        return bool(validators.email(self._word))

    @property
    def is_stop(self):
        return self._word in self._stopword_list

    @property
    def is_oov(self):
        return not self._word in self._probs

    @property
    def is_quote(self):
        return self._word in self._qute_list

    @property
    def is_left_punct(self):
        return self._word in self._left_punct_list

    @property
    def is_right_punct(self):
        return self._word in self._right_punct_list


def read_freqs(freqs_loc, max_length=100, min_doc_freq=5, min_freq=50):
    print("Counting frequencies...")
    counts = PreshCounter()
    total = 0
    with freqs_loc.open() as f:
        for i, line in enumerate(f):
            freq, doc_freq, key = line.rstrip().split("\t", 2)
            freq = int(freq)
            counts.inc(i + 1, freq)
            total += freq
    counts.smooth()
    log_total = math.log(total)
    probs = {}
    with freqs_loc.open() as f:
        for line in tqdm(f):
            freq, doc_freq, key = line.rstrip().split("\t", 2)
            doc_freq = int(doc_freq)
            freq = int(freq)
            if doc_freq >= min_doc_freq and freq >= min_freq and len(key) < max_length:
                word = literal_eval(key)
                smooth_count = counts.smoother(int(freq))
                probs[word] = math.log(smooth_count) - log_total
    oov_prob = math.log(counts.smoother(0)) - log_total
    return probs, oov_prob


def read_clusters(clusters_loc):
    print("Reading clusters...")
    clusters = {}
    with clusters_loc.open() as f:
        for line in tqdm(f):
            try:
                cluster, word, freq = line.split()
                word = ftfy.fix_text(word)
            except ValueError:
                continue
            # If the clusterer has only seen the word a few times, its
            # cluster is unreliable.
            if int(freq) >= 3:
                clusters[word] = cluster
            else:
                clusters[word] = "0"
    # Expand clusters with re-casing
    for word, cluster in list(clusters.items()):
        if word.lower() not in clusters:
            clusters[word.lower()] = cluster
        if word.title() not in clusters:
            clusters[word.title()] = cluster
        if word.upper() not in clusters:
            clusters[word.upper()] = cluster
    return clusters


@plac.annotations(
    lang=("model language", "positional", None, str),
    output_loc=("model output directory", "positional", None, str),
    freqs_loc=("location of words frequencies file", "positional", None, Path),
    clusters_loc=("location of brown clusters data", "positional", None, Path),
)
def main(lang, output_loc, freqs_loc, clusters_loc):
    clusters = read_clusters(clusters_loc)
    probs, oov_prob = read_freqs(freqs_loc)

    with jsonlines.open(output_loc, mode="w") as writer:
        header = {"lang": lang, "settings": {"oov_prob": oov_prob}}

        writer.write(header)

        for word_str, cluster in clusters.items():

            if not word_str:
                continue

            word = Word(word_str, cluster, probs)
            row = {
                "orth": word.orth,  # the word text
                "id": word.id,  # can correspond to row in vectors table
                "lower": word.lower,
                "norm": word.norm,
                "shape": word.shape,
                "prefix": word.prefix,
                "suffix": word.suffix,
                "length": word.length,
                "cluster": word.cluster,
                "prob": word.prob,
                "is_alpha": word.is_alpha,
                "is_ascii": word.is_ascii,
                "is_digit": word.is_digit,
                "is_lower": word.is_lower,
                "is_punct": word.is_punct,
                "is_space": word.is_space,
                "is_title": word.is_title,
                "is_upper": word.is_upper,
                "like_url": word.like_url,
                "like_num": word.like_num,
                "like_email": word.like_email,
                "is_stop": word.is_stop,
                "is_oov": word.is_oov,
                "is_quote": word.is_quote,
                "is_left_punct": word.is_left_punct,
                "is_right_punct": word.is_right_punct,
            }

            writer.write(row)


if __name__ == "__main__":
    plac.call(main)
