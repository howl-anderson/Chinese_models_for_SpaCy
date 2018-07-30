#!/usr/bin/env bash

cd corpus/UD_Chinese-GSD-master

opencc -i zh_gsd-ud-train.conllu -o zh-simplified-ud-train.conllu -c zht2zhs.ini
opencc -i zh_gsd-ud-dev.conllu -o zh-simplified-ud-dev.conllu -c zht2zhs.ini
opencc -i zh_gsd-ud-test.conllu -o zh-simplified-ud-test.conllu -c zht2zhs.ini
