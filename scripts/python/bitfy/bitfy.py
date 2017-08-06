#!/usr/bin/env python
# Python version 3.4+

"""Bitfy
Usage:
    bitfy.py --token=TOKEN [--title=NAME]
    bitfy.py --url=URL [--title=NAME]
    bitfy.py --request=URL [--title=NAME]
    bitfy.py --file=PATH [--title=NAME]
    bitfy.py (-h | --help)
    bitfy.py (-v | --version)

Options:
    -h --help           Show this screen.
    -v --version        Show version.

    -t --token=<TOKEN>  Specifies and saves the token for OAuth connections.
    -u --url=<URL>      Shorten the specified URL.
    -r --request=<URL>  Get data from a request and then shorten all links.
    -f --file=<PATH>    Get data from a file and then shorten all links.

    -title --title=<NAME>   Identifier to use for generated links.

Description:
    Takes in an input, filters out all links and converts them to bit.ly links.

Requirements:
    Python 3.4+, requests, docopt
"""

import sys
import os
import json
import re

import requests

from docopt import docopt


def parse_links(s):
    """
    Returns all links found in an input string.

    Args:
        s (str): input string to search for links in.
    """

    return re.findall(r'(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})', str(s))


def new_link(token, link):
    """
    Creates a new Bitly link.

    Args:
        token (str): Bitly access token.
        link (str): URL to be shortened by Bitly.

    Returns:
        Bitly status information and the returned Bitly link on success.
    """

    r = requests.get("https://api-ssl.bitly.com/v3/shorten?access_token={}&longUrl={}".format(token, link))
    return json.loads(r.content.decode("utf-8"))


def edit_link(token, link, title):
    """
    Edits an already existing Bitly links title.

    Args:
        token (str): Bitly access token.
        link (str): Shortened URL to be edited by Bitly.
        title (str): Updated Bitly link title.

    Returns:
        Bitly status information and the returned Bitly link on success.
    """

    r = requests.get("https://api-ssl.bitly.com/v3/user/link_edit?access_token={}&link={}&edit=title&title={}".format(token, link, title))

    return json.loads(r.content.decode("utf-8"))


def cli():
    args = docopt(__doc__, version="Bitfy 0.2")
    script_dir = os.path.dirname(os.path.abspath(__file__))

    token = args["--token"]
    links = []

    if token:
        f = open(os.path.join(script_dir, "token"), "w")
        f.write(args["--token"])
        f.close()

    elif os.path.isfile(os.path.join(script_dir, "token")):
        f = open(os.path.join(script_dir, "token"), "r")
        token = f.read()
        f.close()

    if args["--url"]:
        links.append(args["--url"])

    if args["--file"]:
        f = open(args["--file"], "r")
        links = links + parse_links(f.read())
        f.close()

    if args["--request"]:
        r = requests.get(args["--request"])

        links = links + parse_links(r.content)

    if links:
        if not token:
            print("Please specify a token before performing an  y commands.")
            return

        for link in links:
            data = new_link(token, link)

            if data["status_code"] != 200:
                print("Error {} on {}: {}".format(data["status_code"], link, data["status_txt"]))
                continue

            domain = link.split("//")[-1].split("/")[0]

            if args["--title"]:
                edit_link(token, data["data"]["url"], "{} - {}".format(args["--title"], domain))
                print("{} - {} | {}".format(args["--title"], domain, data["data"]["url"]))

            else:
                edit_link(token, data["data"]["url"], domain)
                print("{} | {}".format(domain, data["data"]["url"]))


if __name__ == "__main__":
    cli()
