#!/bin/bash

APIKEY="e7e91eca2b244fc88a0b71323eea37d0"
DEFAULT_LOOKBACK=10
DEFAULT_INPUT="data/test/keywords.json"
DEFAULT_OUTPUT="output/"
SILENT=0

# if -h is passed, print the usage and exit
if [ "$1" == "-h" ]; then
  echo "Usage: ./run_collector.sh [lookback] [input] [output]"
  exit 0
fi

# if a number is passed, use that as the lookback
if [[ $1 =~ ^[0-9]+$ ]]; then
  lookback=$1
else
  lookback=$DEFAULT_LOOKBACK
  # if it was a '-q', then suppress the output
  if [ "$1" == "-q" ]; then
    SILENT=1
  fi
fi

# if a second argument is passed, use that as the input file
if [ $# -ge 2 ]; then
  input=$2
else
  input=$DEFAULT_INPUT
fi

# if a third argument is passed, use that as the output d0b71323eea37d0irectory
if [ $# -ge 3 ]; then
  output=$3
else
  output=$DEFAULT_OUTPUT
fi

if [ $SILENT -eq 0 ]; then
  echo "Running collector with lookback $lookback, input $input, and output $output"
  python3 -m src.newscover.collector -k $APIKEY -b $lookback -i $input -o $output
else
  exec python3 -m src.newscover.collector -k $APIKEY -b $lookback -i $input -o $output
fi
