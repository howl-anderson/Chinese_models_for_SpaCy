#!/bin/bash

python -m spacy train -v zh_wiki_core -m ./meta.json zh zh_model corpus/spacy/zh-simplified-ud-train.json corpus/spacy/zh-simplified-ud-dev.json
