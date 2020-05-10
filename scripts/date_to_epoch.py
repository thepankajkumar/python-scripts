#!/usr/local/bin/python3

from datetime import datetime
import argparse
from argparse import Namespace


def convert_to_epoch(date_time: str) -> float:
    try:
        return datetime.fromisoformat(date_time).timestamp()
    except ValueError:
        print("Date could not be parsed. Please provide it in ISO 8601 format")
        raise


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("date_time", help="Datetime to convert to timestamp (YY-mm-dd%HH:MM:SS or YY-mm-dd format)", type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    timestamp = convert_to_epoch(args.date_time)
    print(str(int(timestamp)))


if __name__ == "__main__":
    main()