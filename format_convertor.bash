#!/bin/bash

mkdir -p corpus/spacy

python -m spacy convert corpus/UD_Chinese-GSD-master/zh-simplified-ud-train.conllu corpus/spacy
python -m spacy convert corpus/UD_Chinese-GSD-master/zh-simplified-ud-dev.conllu corpus/spacy
python -m spacy convert corpus/UD_Chinese-GSD-master/zh-simplified-ud-test.conllu corpus/spacy
