#!/bin/bash

DESCRIPTION="This script will another script on all of the files in the input folder"
USAGE="Usage: $0 <input_folder> <script_to_run>"

# if no arguments supplied, echo usage
if [ $# -ne 2 ]; then
    echo $USAGE
    exit 1
fi

# if argument is not a directory, echo usage
if [ ! -d "$1" ]; then
    echo $USAGE
    exit 1
fi

# if argument is not a file, echo usage
if [ ! -f "$2" ]; then
    echo $USAGE
    exit 1
fi

folder=$1
script=$2

for file in $folder/*
do
  filename=$(basename -- $file)
  echo $filename
  ./$script $file
done
