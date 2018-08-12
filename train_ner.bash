#!/bin/bash

python -m spacy train zh ner_model china_ner_train.json china_ner_eval.json --no-tagger --no-parser -verbose True -g 0 --vectors ./zh_model
