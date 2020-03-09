#!/usr/bin/env bash

cd corpus/UD_Chinese-GSD-master

opencc -i zh_gsd-ud-train.conllu -o zh-simplified-ud-train.conllu -c t2s.json
opencc -i zh_gsd-ud-dev.conllu -o zh-simplified-ud-dev.conllu -c t2s.json
opencc -i zh_gsd-ud-test.conllu -o zh-simplified-ud-test.conllu -c t2s.json
