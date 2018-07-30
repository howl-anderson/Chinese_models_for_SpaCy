#!/bin/bash

python -m spacy train zh zh_wiki_core/model-final china_ner_train.json china_ner_eval.json --no-tagger --no-parser
