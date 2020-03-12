import plac
import gensim
from gensim import utils


class Corpus:
    def __init__(self, corpus_file):
        self.corpus_file = corpus_file

    def __iter__(self):
        with open(self.corpus_file) as fd:
            for line in fd:
                yield utils.simple_preprocess(line)


@plac.annotations(
    in_dir=("Location of input directory"),
    out_loc=("Location of output file"),
    n_workers=("Number of workers", "option", "n", int),
    size=("Dimension of the word vectors", "option", "d", int),
    window=("Context window size", "option", "w", int),
    min_count=("Min count", "option", "m", int),
    negative=("Number of negative samples", "option", "g", int),
    nr_iter=("Number of iterations", "option", "i", int),
)
def main(
    in_dir,
    out_loc,
    negative=5,
    n_workers=4,
    window=5,
    size=128,
    min_count=10,
    nr_iter=2,
):
    sentences = Corpus(in_dir)
    model = gensim.models.Word2Vec(
        sentences=sentences,
        size=size,
        window=window,
        min_count=min_count,
        workers=n_workers,
        sample=1e-5,
        negative=negative,
        iter=nr_iter,
    )
    model.wv.save_word2vec_format(out_loc, binary=False)


if __name__ == "__main__":
    plac.call(main)
