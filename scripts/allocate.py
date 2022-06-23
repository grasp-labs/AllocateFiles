#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
from typing import Dict

import requests

from config import configuration, Config
from libs.authorization import get_access_token


def upload(file_obj: Dict, params: Dict, config: Config = configuration) -> requests.Response:
    headers = get_access_token(config=config)
    return requests.post(
        config.service_url,
        files=file_obj,
        params=params,
        headers=headers
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Subscription service allocate file assets",
        description="Sample script for uploading files.",
        epilog="File should momentarily be available for consumption."
    )
    parser.add_argument("--f", type=str, help="Specify file format suffix")
    parser.add_argument("--o", type=str, help="Json file orientation", required=False)
    parser.add_argument("--d", type=str, help="CSV file delimiter", required=False)
    parser.add_argument("--i", type=str, help="Primary key in file", default="id")
    args = vars(parser.parse_args())
    if args.get("f") not in ["csv", "json", "parquet"]:
        raise AttributeError("Unsupported file format argument --f ")

    if args.get("f") == "json" and not args.get("o"):
        raise AttributeError("Specify orient --o for JSON files.")

    if args.get("f") == "csv" and not args.get("d"):
        raise AttributeError("Specify delimiter --d for CSV files.")

    file_path = Path(__file__).resolve().parent.parent / f"samples/sample.{args.get('f')}"
    parameters = {
        "file_name": f"sample.{args.get('f')}",
        "owner_id": "123XY",
        "fmt": args.get('f'),

    }
    if args.get("o"):
        parameters["orient"] = args.get("o")

    if args.get("d"):
        parameters["delimiter"] = args.get("d")

    if args.get("i"):
        parameters["index_key"] = args.get("i")

    _file = open(file_path, "rb")
    data = {"file": _file}
    response = upload(file_obj=data, params=parameters)
    if response.status_code != 201:
        print(f"Oh no.. {response.status_code} {response.content}")
    else:
        print(f"Success! .. {response.status_code} {response.content}")
