# COMP370 Homework 6 - Data Collection

Python project to query newsapi.org API
You need an api key to run this project. You can get one [here](https://newsapi.org/)

This repo contains

- A python CLI tool to query newsapi.org
- A test suite

## TODO

- Containerize

## Pitfalls

- Don't forget to [generate your own api_key](https://newsapi.org/)

# Setup/Installation

## Python Installation

`python -m venv venv`

`python -m pip install -r requirements.txt`

`python -m src/newscover.collector.py -h` for info on the tool

# Running

## CLI tool

A tool that can call newsapi.org and filter the output based on keywords and dates

`src/newscover/collector.py`

### Running

`python -m src.newscover.collector -h` for help

## Scripts

All of these tools have a usage message

### `run_collector.sh`

Is a useful tool run automatically run the CLI with default values, faster to use than the CLI if running multiple times with different values

Don't forget to add your api_key to the script

### `get_individual_dates.sh`

Is a tool to check all dates in json file

### `run_script_on_folder.sh`

Is a useful tool to verify that you are getting appropriate dates from the CLI tool
