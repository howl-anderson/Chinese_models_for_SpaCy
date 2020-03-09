#!/bin/bash

cpu_count=`nproc --all`
process_count=$(expr $cpu_count - 1)

./third-part/brown-cluster/wcluster --text WORDS.txt --c 1000 --threads ${process_count}
