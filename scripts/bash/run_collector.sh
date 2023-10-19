#!/bin/bash

APIKEY="e7e91eca2b244fc88a0b71323eea37d0"
DEFAULT_LOOKBACK=1
DEFAULT_INPUT="data/test/keywords.json"
DEFAULT_OUTPUT="output/"

# if -h is passed, print the usage and exit
if [ "$1" == "-h" ]; then
  echo "Usage: ./run_collector.sh [lookback] [input] [output]"
  exit 0
fi

# if an int is passed as the first argument, use that as the lookback
if [ $# -eq 1 ]; then
  lookback=$1
else
  lookback=$DEFAULT_LOOKBACK
fi

# if a second argument is passed, use that as the input file
if [ $# -eq 2 ]; then
  input=$2
else
  input=$DEFAULT_INPUT
fi

# if a third argument is passed, use that as the output d0b71323eea37d0irectory
if [ $# -eq 3 ]; then
  output=$3
else
  output=$DEFAULT_OUTPUT
fi

exec python3 -m src.newscover.collector -k $APIKEY -b $lookback -i $input -o $output
