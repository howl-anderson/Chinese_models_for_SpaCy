#!/bin/bash

python -m spacy init-model zh spacy_models/base_model --jsonl-loc ./spacy_corpus.jsonl --vectors-loc WORDS_VECS.txt --vectors-name zh_core_web_sm.vectors
