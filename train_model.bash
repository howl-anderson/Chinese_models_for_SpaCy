#!/bin/bash

python -m spacy train zh depedency_model corpus/spacy/zh-simplified-ud-train.json corpus/spacy/zh-simplified-ud-dev.json -v zh_model -m ./meta.json --no-entities
