# SpaCy Chinese model training workflow

## get preprocessed Chinese Wikipedia corpus
   see project [chinese-wikipedia-corpus-creator](https://github.com/howl-anderson/chinese-wikipedia-corpus-creator) for more details.

## computing word frequency
   * input: `token_cleaned_plain_files/*`
   * output: `WORDS_FREQ.txt`
   * script: `compute_words_freq.bash`

## merge all files into one
   * input: `token_cleaned_plain_files/*`
   * output: `WORDS.txt`
   * script: `merge_all_text_files.bash`

## compute brown cluster
### brown cluster computing software
   Official software is [brown-cluster](https://github.com/percyliang/brown-cluster).

### install
   * input: -
   * output: ``
   * script: `download_and_compile_brown_cluster.bash`

### computing
   * input: `WORDS.txt`
   * output: `WORDS-c1000-p1.out/*`
   * script: `compute_brown_cluster.bash`

## compute word vector
   * input: `token_cleaned_plain_files/*`
   * output: `WORDS_VECS.txt`
   * script: `compute_plain_word_vec.bash`

## initial SpaCy model
   * input: `./WORDS-c1000-p1.out/paths  WORDS_VECS.txt  WORDS_FREQ.txt`
   * output: `zh_wiki_core/**/*`
   * script: `create_init_model.bash`

## getting UD_Chinese-GSD corpus

### download
   * input: -
   * output: `corpus/UD_Chinese-GS.zip`
   * script: `download_UD_Chinese-GSD_corpus.bash`

### extracting
   * input: `corpus/UD_Chinese-GSd.zip`
   * output: `corpus/UD_Chinese-GSd`
   * script: `extract_UD_Chinese-GSD_corpus.bash`

### convert to simplified Chinese
   * input: `corpus/UD_Chinese-GSd/zh-ud-*.conllu`
   * output: `corpus/UD_Chinese-GSd/zh-simplified-ud-*.conllu`
   * script: `convert_UD_Chinese-GSd_corpus.bash`

## convert UD corpus format
   * input: `.corpus/UD_Chinese-GSD/zh-simplified-ud-*.conllu`
   * output: `corpus/spacy/zh-simplified-ud-*.conllu`
   * script: `format_convertor.bash`

## train SpaCy model
   * input: `zh_wiki_core  corpus/spacy/zh-simplified-ud-*.conllu`
   * output: `zh_model`
   * script: `train_model.bash`
