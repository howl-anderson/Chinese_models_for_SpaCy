# SpaCy Chinese model training workflow

## get preprocessed Chinese Wikipedia corpus
   see project [chinese-wikipedia-corpus-creator](https://github.com/howl-anderson/chinese-wikipedia-corpus-creator) for more details.
   
### produce wikipedia corpus ###
   * input: -
   * output: `token_cleaned_plain_files/`
   * script: `create_wikipedia_corpus.bash`

### copy corpus to workspace ###
   * input: `chinese-wikipedia-corpus-creator/token_cleaned_plain_files/``
   * output: `token_cleaned_plain_files/`
   * script: `move_wikipedia_corpus.bash`

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

### build base model
   * input: `./WORDS-c1000-p1.out/paths  WORDS_VECS.txt  WORDS_FREQ.txt`
   * output: `spacy_models/base_model/**/*`
   * script: `create_init_model.bash`
   
### modify model name
   * input: `spacy_models/base_model/meta.json`
   * output: `spacy_models/base_model/meta.json`
   * script: `update_model_meta.py`
   

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

## merge sub-model
   * input: `spacy_models/dependency_model`, `spacy_models/ner_model`
   * output: `spacy_models/final_model`
   * script: `merge_submodel.py`

## create package 
   * input: `spacy_models/final_model/`
   * output: `spacy_package/`
   * script: `./create_model_package.bash`
