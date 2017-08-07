#!/usr/bin/env python
# Python version 3.4+

"""Seqcrawl
Usage:
    seqcrawl.py <url> <characters> <length>
                [--start <number>]
                [--end <number>]
                [--log <path>]
                [--sleep <number>]
    seqcrawl.py (-h | --help)
    seqcrawl.py (-v | --version)

Options:
    -h --help         Show this screen.
    -v --version      Show version.

    --start <number>  Sequence generation iteration to start at.
    --end <number>    Sequence generation iteration to complete at.
    --log <path>      Log file to write information to.
    --sleep <number>  Time between crawl requests to sleep.

Description:
    Crawls an entry point URL using generated fixed length sequences from an
    input character set.

Requirements:
    Python 3.4+, requests, docopt
"""

import os
import time

import requests

from docopt import docopt
from datetime import datetime


def cli():
    args = docopt(__doc__, version="Seqcrawl 0.2")
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Handle arguments.
    url = args["<url>"]
    chars = args["<characters>"]
    length = args["<length>"]

    # Handle optional arguments.
    start = args["--start"] or 0
    end = args["--end"] or False
    sleep = args["--sleep"] or 1.5
    log = args["--log"] or False

    try:
        txt = crawl(baseurl=url, iteration=int(start), iteration_end=end, set_chars=chars, set_length=int(length), sleep_time=float(sleep))

        # Print information about the current execution of the script.
        print(txt)

        if log:
            # Log the current run in a file.
            with open(os.path.join(script_dir, log), 'a') as f:
                f.write(txt)

    except KeyboardInterrupt:
        pass


def sizeofh(num, suffix="B"):
    """
    Generate a human readable sizeof format.

    Args:
        num (number): input number of bytes to convert.
        suffix (str): suffix of the output format.

    Returns:
        String containing the correctly formatted sizeof.
    """

    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0

    return "%.1f%s%s" % (num, 'Yi', suffix)


def generate(set_chars, set_length, iteration=0):
    """
    Generates a set length sequence of characters from an input character set
    based on an input iteration.

    Args:
        set_chars (str): input character set to construct further sets from.
        set_length (int): length of the character set to output and generate.
        iteration (int): current iteration of the construction algorithm.

    Returns:
        The generated character sequence.
    """

    s = ""  # Current selection from the input character set.

    # Number of characters in the character set.
    charcount = len(set_chars)

    # Iterate over the desired length of the output combination and generate the combination.
    for i in range(0, set_length):
        char = setchars[int((iteration / pow(charcount, set_length - i - 1)) % charcount)]

        if char is not " ":
            s = s + char

    return s


def crawl(baseurl, set_chars, set_length, iteration_start=0, iteration_end=False, sleep_time=1.5):
    """
    Crawls an input URL entry point by iterating over fixed length combinations
    of an input character set.

    Args:
        baseurl (str): entry point URL to base further connections off of.
        set_chars (str): input character set to construct further sets from.
        set_length (int): length of the character set to output and generate.
        iteration_start (int): current iteration of the construction algorithm.
        iteration_end (int): optional iteration to complete at.
        sleep_time (number): sleep time between requests to avoid spamming.
    """

    totalsize = 0
    totalcount = 0

    # Number of characters in the character set.
    charcount = len(set_chars)

    iteration = 0
    iteration_end = int(iteration_end) if iteration_end else pow(charcount, set_length)

    # Get the current time for the timeout calculation.
    time_last = datetime.now()

    # Start iterating until we reach the max iterations.
    while iteration < iteration_end:
        # Skip iterations if we are catching up.
        if iteration < iteration_start:
            continue

        # Generate the current set.
        selection = generate(set_chars, set_length, iteration)

        # Current iteration step.
        iteration = iteration + 1

        # Calculate the current time since the last loop.
        time_elapsed = (datetime.now() - time_last).total_seconds()

        # Check if enough time has past. Else, sleep until the time is up.
        if time_elapsed < sleep_time:
            time.sleep(sleep_time - time_elapsed)

        # Store the current time for the next loop.
        time_last = datetime.now()

        # Make the request.
        data = requests.get("{}{}".format(baseurl, selection))

        # Print the current file.
        print("{}. {} - {}".format(iteration, selection, sizeofh(len(data.content))))

        # Only write data if we had a good response code.
        if data.status_code == 200:
            with open(selection, 'wb') as f:
                # Write the output file.
                for chunk in data:
                    f.write(chunk)

        totalcount = totalcount + 1
        totalsize = totalsize + len(data.content)

    return "{} | Range: {} - {} | Total files: {} | Total size: {}\n".format(datetime.now(), iteration_start + 1, iteration, totalcount, sizeofh(totalsize))


if __name__ == "__main__":
    cli()
