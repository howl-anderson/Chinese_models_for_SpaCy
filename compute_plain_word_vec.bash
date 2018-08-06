#!/bin/bash

# TODO: process number shoud auto compute
python ./spacy-dev-resources/training/plain_word_vectors.py -i 200 -n 6 ../chinese-wikipedia-corpus-creator/token_cleaned_plain_files WORDS_VECS.txt
