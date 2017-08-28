#!/usr/bin/env python
# Python version 3.5+

"""Zipcrack
Usage:
    zipcrack.py <file> (--sequence=STRING --length=NUMBER | --dictionary=PATH)
                [--iteration-start=NUMBER]
                [--iteration-end=NUMBER]
                [--sleep=NUMBER]
                [--output=PATH]
    zipcrack.py (-h | --help)
    zipcrack.py (-v | --version)

Options:
    -h --help                 Show this screen.
    -v --version              Show version.

    --iteration-start=NUMBER  Iteration to start at.
    --iteration-end=NUMBER    Iteration to complete at.
    --sleep=NUMBER            Time between attempts to sleep.
    --output=PATH             Output directory to extract to.

Description:
    Generates character sequences to brute force crack a zip archive.

Requirements:
    Python 3.5+, docopt
"""

import zipfile

import os
import time
import math

from docopt import docopt
from datetime import datetime


def cli():
    args = docopt(__doc__, version="Zipcrack 0.2")
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Handle arguments.
    filepath = args["<file>"]

    # Handle sequence arguments.
    chars = args["--sequence"] or False
    length = args["--length"] or 4

    # Handle dictionary arguments.
    dictionary = args["--dictionary"] or False

    # Handle optional arguments.
    begin = args["--iteration-start"] or 0
    end = args["--iteration-end"] or False
    sleep = args["--sleep"] or 0
    output = args["--output"] or os.path.dirname(os.path.realpath(__file__))

    try:
        if chars:
            crack_sequence(
                filepath=filepath,
                outpath=output,
                set_chars=chars,
                set_length=int(length),
                iteration_start=int(begin),
                iteration_end=end,
                sleep_time=float(sleep)
            )

        if dictionary:
            crack_dictionary(
                filepath=filepath,
                outpath=output,
                dictpath=dictionary,
                iteration_start=int(begin),
                iteration_end=end,
                sleep_time=float(sleep)
            )

    except KeyboardInterrupt:
        pass


def generate_sequence(set_chars, set_length, iteration=0):
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
        char = set_chars[int((iteration / pow(charcount, set_length - i - 1)) % charcount)]
        if char is not " ":
            s = s + char

    return s


def crack_sequence(filepath, outpath, set_chars, set_length, iteration_start=0, iteration_end=False, sleep_time=0):
    """
    Attempts to use generated character sequences from an input sequence to
    crack a zip archive's password.

    Args:
        filepath (str): input file to attempt sequence cracking on.
        set_chars (str): input character set to construct further sets from.
        set_length (int): length of the character set to output and generate.
        iteration_start (int): optional starting iteration of the construction algorithm.
        iteration_end (int): optional iteration to complete at.
        sleep_time (number): optional sleep time between crack attempts.
    """

    # Number of characters in the character set.
    charcount = len(set_chars)

    iteration = 0
    iteration_end = int(iteration_end) if iteration_end else pow(charcount, set_length)

    # Get the current time for the timeout calculation.
    time_last = datetime.now()

    zip_file = zipfile.ZipFile(filepath)

    print("Running crack with {} generated sequences.".format(iteration_end))

    # Start iterating until we reach the max iterations.
    while iteration < iteration_end:
        # Skip iterations if we are catching up.
        if iteration < iteration_start:
            continue

        # Generate the current set.
        password = generate_sequence(set_chars, set_length, iteration)

        # Current iteration step.
        iteration = iteration + 1

        # Calculate the current time since the last loop.
        time_elapsed = (datetime.now() - time_last).total_seconds()

        # Check if enough time has past. Else, sleep until the time is up.
        if time_elapsed < sleep_time:
            time.sleep(sleep_time - time_elapsed)

        # Store the current time for the next loop.
        time_last = datetime.now()

        try:
            zip_file.extractall(outpath, pwd=password.encode("utf-8", "replace"))

            print("Password found: {}".format(password))
            return

        except:
            print("{}. {}\033[K\r".format(iteration, password), end="", flush=False)

    print("\nPassword not found.")


def crack_dictionary(filepath, outpath, dictpath, iteration_start=0, iteration_end=False, sleep_time=0):
    """
    Attempts to use lines from a dictionary file to crack a zip archive's password.

    Args:
        filepath (str): input file to attempt dictionary cracking on.
        dictpath (str): input dictionary file to read from.
        iteration_start (int): optional line of the dictionary to start from.
        iteration_end (int): optional iteration to complete at.
        sleep_time (number): optional sleep time between crack attempts.
    """

    iteration = 0
    iteration_end = int(iteration_end) if iteration_end else math.inf

    # Get the current time for the timeout calculation.
    time_last = datetime.now()

    zip_file = zipfile.ZipFile(filepath)

    with open(dictpath, "r", encoding="utf-8") as f:
        for line in f.readlines():
            # Skip iterations if we are catching up.
            if iteration < iteration_start:
                continue

            # Stop iterating if the limit is passed.
            if iteration > iteration_end:
                return

            # Current iteration step.
            iteration = iteration + 1

            # Get the dictionary line.
            password = line.strip("\n")

            # Calculate the current time since the last loop.
            time_elapsed = (datetime.now() - time_last).total_seconds()

            # Check if enough time has past. Else, sleep until the time is up.
            if time_elapsed < sleep_time:
                time.sleep(sleep_time - time_elapsed)

            # Store the current time for the next loop.
            time_last = datetime.now()

            try:
                zip_file.extractall(outpath, pwd=password.encode("utf-8", "replace"))

                print("Password found: {}".format(password))
                return

            except:
                print("{}. {}\033[K\r".format(iteration, password), end="", flush=False)

        print("\nPassword not found.")


if __name__ == "__main__":
    cli()
