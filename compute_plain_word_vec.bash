#!/bin/bash

# TODO: process number shoud auto compute
python ./spacy-dev-resources/training/plain_word_vectors.py -i 2 -n 39 token_cleaned_plain_files WORDS_VECS.txt
