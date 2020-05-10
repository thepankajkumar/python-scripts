#!/usr/local/bin/python3

import jwt
import argparse
from argparse import Namespace
import json
import datetime
from jwt.exceptions import DecodeError


def parse_token(token: str) -> None:
    try:
        result = jwt.decode(token, verify=False)
    except DecodeError:
        print("Failed to decode token")
        return

    exp = result.get('exp', None)
    if exp and isinstance(exp, (int)):
        local_time = datetime.datetime.fromtimestamp(
            exp).strftime('%Y-%m-%d %H:%M:%S')
        result['exp'] = str(exp) + " (" + local_time + ")"
    print(json.dumps(result, indent=4, sort_keys=False))


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="JWT Token to decode")
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    parse_token(args.token)


if __name__ == "__main__":
    main()