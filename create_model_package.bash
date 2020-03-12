#!/bin/bash

python -m spacy package spacy_models/final_model spacy_package --force

cd spacy_package/zh_core_web_sm-0.1.0
python ./setup.py sdist
