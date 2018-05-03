#!/bin/bash

python -m spacy convert ../UD_Chinese-GSD/zh-simplified-ud-train.conllu .
python -m spacy convert ../UD_Chinese-GSD/zh-simplified-ud-dev.conllu .
python -m spacy convert ../UD_Chinese-GSD/zh-simplified-ud-test.conllu .
