#!/usr/bin/env bash

python -m spacy init-model zh zh_model/ WORDS_FREQ.txt -c WORDS-c1000-p1.out/paths -v WORDS_VECS.txt
