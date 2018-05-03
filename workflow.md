# SpaCy Chinese model trainning workflow
## get preprocessed Chinese wikipedia corpus
	see project [chinese-wikipedia-corpus-creator](https://github.com/howl-anderson/chinese-wikipedia-corpus-creator) for more details.
## computting word frequence
    * input: `token_cleaned_plain_files/*`
    * output: `WORDS_FREQ.txt`
    * script: `compute_words_freq.bash`
## merge all files into one
    * input: `token_cleaned_plain_files/*`
    * output: `WORDS.txt`
    * script: `merge_all_text_files.bash`
## compute brown cluster
    * input: `WORDS.txt`
    * output: `WORDS-c1000-p1.out/*`
    * script: `compute_brown_cluster.bash`
## compute word vector
    * input: `token_cleaned_plain_files/*`
    * output: `WORDS_VECS.txt`
    * script: `compute_plain_word_vec.bash`
## initial Spacy model
    * input: `./WORDS-c1000-p1.out/paths  WORDS_VECS.txt  WORDS_FREQ.txt`
	* output: `zh_wiki_core/**/*`
	* script: `create_init_model.bash`
## convert UD corpus format
    * input: `../UD_Chinese-GSD/zh-simplified-ud-*.conllu`
	* output: `zh-simplified-ud-*.conllu`
	* script: `format_convertor.bash`
## train Spacy model
    * input: `zh_wiki_core  zh-simplified-ud-*.conllu`
	* output: `zh_model`
	* script: `train_model.bash`
