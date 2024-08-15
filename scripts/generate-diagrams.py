#!/bin/bash

find . -type f -name '*.diagrams.py' | while read file; do
    directory=${file%/*}
    filename=${file##*/}
    pushd ${directory}
    docker run --rm -v "$PWD":/diagrams/scripts/ -w /diagrams/scripts/ mjdk/diagrams ${filename}
    popd
done
