#!/bin/bash

# This script will return all the unique dates from a file containing json data

Usage="Usage: ./get_individual_dates.sh $0"

function usage {
  echo $Usage
  exit 1
}

if [ $# -ne 1 ]; then
  usage
fi

grep 'publishedAt' $1 | grep -o -P "\d{4}-\d{2}-\d{2}" | sort | uniq
