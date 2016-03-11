# -*- coding: utf-8 -*-
# This file is part of https://github.com/26fe/jsonstat.py
# Copyright (C) 2016 gf <gf@26fe.com>
# See LICENSE file

# stdlib
from __future__ import print_function
import os
import sys

# external modules
import click

# jsonstat
JSONSTAT_HOME = os.path.join(os.path.dirname(__file__), '..', '..')
try:
    import jsonstat
except ImportError:
    sys.path.append(JSONSTAT_HOME)
    import jsonstat


@click.command()
@click.option('--cache_dir', default='./data', help='where to store downloaded files')
@click.argument('urls', nargs=-1)
def jsonstat_cli(cache_dir, urls):
    if len(urls) == 0:
        urls = ['http://json-stat.org/samples/oecd-canada.json']

    url = urls[0]

    # cache_dir = os.path.abspath(os.path.join(JSONSTAT_HOME, "tmp"))
    # print("cache_dir is '{}'".format(cache_dir))
    d = jsonstat.cache_dir(cache_dir)
    print("downloaded file(s) are stored into '{}'".format(d))

    print("download '{}'".format(url))
    collection = jsonstat.from_url(url)
    print(collection)


if __name__ == "__main__":
    jsonstat_cli()
