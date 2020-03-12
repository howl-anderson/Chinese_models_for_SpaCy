#!/bin/bash

python -m spacy train zh spacy_models/dependency_model corpus/spacy/zh-simplified-ud-train.json corpus/spacy/zh-simplified-ud-dev.json --pipeline tagger,parser -v spacy_models/base_model -m meta.json -V 0.1.0 -n 1
