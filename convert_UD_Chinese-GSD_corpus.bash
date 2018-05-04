#!/usr/bin/env bash

cd corpus/UD_Chinese-GS

opencc -i zh-ud-train.conllu -o zh-simplified-ud-train.conllu -c zht2zhs.ini
opencc -i zh-ud-dev.conllu -o zh-simplified-ud-dev.conllu -c zht2zhs.ini
opencc -i zh-ud-test.conllu -o zh-simplified-ud-test.conllu -c zht2zhs.ini
