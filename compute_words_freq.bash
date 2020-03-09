#!/bin/bash

cpu_count=`nproc --all`
process_count=$(expr $cpu_count - 1)

python ./spacy-dev-resources/training/plain_word_freqs.py -n ${process_count} token_cleaned_plain_files WORDS_FREQ.txt
