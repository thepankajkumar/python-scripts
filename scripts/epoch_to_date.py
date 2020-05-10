#!/usr/local/bin/python3

from datetime import datetime
import argparse
from argparse import Namespace


def convert_to_date(epoch: int) -> str:
    try:
        return datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        #Could be in milliseconds
        return datetime.utcfromtimestamp(epoch/1000).strftime('%Y-%m-%dT%H:%M:%SZ')


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("epoch", help="Epoch time to convert", type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    date = convert_to_date(args.epoch)
    print(date)


if __name__ == "__main__":
    main()