#!/bin/bash

cpu_count=`nproc --all`
process_count=$(expr $cpu_count - 1)

python ./spacy-dev-resources/training/plain_word_vectors.py -i 200 -n ${process_count} ./WORDS.txt WORDS_VECS.txt
