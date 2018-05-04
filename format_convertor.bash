#!/bin/bash

mkdir -p corpus/spacy

python -m spacy convert corpus/UD_Chinese-GSD/zh-simplified-ud-train.conllu corpus/spacy
python -m spacy convert corpus/UD_Chinese-GSD/zh-simplified-ud-dev.conllu corpus/spacy
python -m spacy convert corpus/UD_Chinese-GSD/zh-simplified-ud-test.conllu corpus/spacy
