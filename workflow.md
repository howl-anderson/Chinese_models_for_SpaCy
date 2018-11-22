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

## initial SpaCy model [TODO: may be removed]
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
   * script: `convert_UD_Chinese-GSD_corpus.bash`

## convert UD corpus format
   * input: `.corpus/UD_Chinese-GSD/zh-simplified-ud-*.conllu`
   * output: `corpus/spacy/zh-simplified-ud-*.conllu`
   * script: `format_convertor.bash`

## init spacy model with word vector & word cluster & word frquence
   * input: `WORDS_FREQ.txt`, `WORDS-c1000-p1.out/paths`, `WORDS_VECS.txt`
   * output: `zh_model/*`
   * script: `init_model.bash`

## train SpaCy model for POS and dependency parser
   * input: `zh_model  corpus/spacy/zh-simplified-ud-*.conllu`
   * output: `dependency_model`
   * script: `train_model.bash`

## translate onotNote 5 to spacy json file
   * input: `TODO` 
   * output: `TODO`
   * script: `onto_to_spacy_json.bash`

## train SpaCy model for NER parser
   * input: `zh_model china_ner_train.json china_ner_eval.json`
   * output: `ner_model`
   * script: `train_ner.bash`
