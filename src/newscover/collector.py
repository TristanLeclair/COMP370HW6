import argparse
import json

from src.newscover.utils import dir_path
from src.newscover.newsapi import fetch_latest_news


def main():
    (api_key, lookback_days, input_file, output_dir) = parse_args()

    # read input file
    keywords_dict = json.load(input_file)

    # for each keyword list, query newsapi.org and write the results to a json file
    for key, value in keywords_dict.items():
        news = fetch_latest_news(api_key, value, lookback_days)
        with open(f"{output_dir}/{key}.json", "w") as f:
            json.dump(news, f, indent=4, sort_keys=True)


def parse_args():
    parser = argparse.ArgumentParser(prog="Collector", description="Query newsapi.org")

    parser.add_argument(
        "-k", metavar="<api_key>", help="api key", required=True, type=str
    )
    parser.add_argument(
        "-b",
        metavar="<# of days to lookback>",
        help="# of days to lookback, default is 10",
        required=False,
        type=int,
        default=10,
    )
    parser.add_argument(
        "-i",
        metavar="<input_file>",
        help="json file containing a dictionary of named keyword lists.",
        type=argparse.FileType("r"),
        required=True,
    )
    parser.add_argument(
        "-o",
        metavar="<output_dir>",
        help="the output directory to which to write all the json files to",
        type=dir_path,
        required=True,
    )

    args = parser.parse_args()

    api_key = args.k
    lookback_days = args.b
    file = args.i
    output_dir = args.o

    return (api_key, lookback_days, file, output_dir)


if __name__ == "__main__":
    main()
