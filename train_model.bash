#!/bin/bash

python -m spacy train -v zh_wiki_core -m ./meta.json zh zh_model ./zh-simplified-ud-train.json ./zh-simplified-ud-dev.json
