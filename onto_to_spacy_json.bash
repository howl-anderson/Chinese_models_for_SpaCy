#!/usr/bin/env bash

python onto_to_spacy_json.py -i "./ontonotes-release-5.0/data/files/data/chinese/annotations/" -t "china_ner_train.json" -e "china_ner_eval.json" -v 0.05
