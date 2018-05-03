#!/bin/bash

python -m spacy init-model -c ./WORDS-c1000-p1.out/paths -v WORDS_VECS.txt zh zh_wiki_core WORDS_FREQ.txt
