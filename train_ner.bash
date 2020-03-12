#!/bin/bash

python -m spacy train zh spacy_models/ner_model ./china_ner_train.json ./china_ner_eval.json --pipeline ner -m meta.json -v ./spacy_models/dependency_model/model-best -n 1
