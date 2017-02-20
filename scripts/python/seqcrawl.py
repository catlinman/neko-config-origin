
"""Seqcrawl
Usage:
    seqcrawl.py --url=URL --chars=CHARS --length=LENGTH
                [--start=START]
                [--end=END]
                [--out=OUT]
                [--wait=WAIT]
    seqcrawl.py (-h | --help)
    seqcrawl.py (-v | --version)

Options:
    -h --help               Show this screen.
    -v --version            Show version.

    -u --url=<URL>          Entry point URL to use.
    -c --chars=<CHARS>      Character set to use for generation of sequences.
    -l --length=<LENGTH>    Length of generated character sequences.

    -s --start<START>       Sequence generation iteration to begin at.
    -e --end<END>           Optional sequence generation iteration to complete at.
    -o --out<OUT>           Optional log file to write information to.
    -w --wait<WAIT>         Optional time between crawl requests to sleep and wait.

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
    args = docopt(__doc__, version="Seqcrawl 0.1")
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Handle arguments.
    url = args["--url"]
    chars = args["--chars"]
    length = args["--length"]

    # Handle optional arguments.
    start = args["--start"] or 0
    end = args["--end"] or False
    wait = args["--wait"] or 1.5
    out = args["--out"] or False

    try:
        txt = crawl(baseurl=url, iteration=int(start), enditeration=end, setchars=chars, setlength=int(length), sleeptime=float(wait))

        # Print information about the current execution of the script.
        print(txt)

        if out:
            # Log the current run in a file.
            with open(os.path.join(script_dir, out), 'a') as f:
                f.write(txt)

    except KeyboardInterrupt:
        pass


def sizeofh(num, suffix="B"):
    '''
    Generate a human readable sizeof format.

    Args:
        num (number): input number of bytes to convert.
        suffix (str): suffix of the output format.

    Returns:
        String containing the correctly formatted sizeof.
    '''

    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0

    return "%.1f%s%s" % (num, 'Yi', suffix)


def generate(setchars, setlength, iteration=0):
    '''
    Generates a set length sequence of characters from an input character set
    based on an input iteration.

    Args:
        setchars (str): input character set to construct further sets from.
        setlength (int): length of the character set to output and generate.
        iteration (int): current iteration of the construction algorithm.

    Returns:
        The generated character sequence.
    '''

    s = ""  # Current selection from the input character set.

    # Number of characters in the character set.
    charcount = len(setchars)

    # Iterate over the desired length of the output combination and generate the combination.
    for i in range(0, setlength):
        s = s + setchars[int((iteration / pow(charcount, setlength - i - 1)) % charcount)]

    return s


def crawl(baseurl, setchars, setlength, iteration=0, enditeration=False, sleeptime=1.5):
    '''
    Crawls an input URL entry point by iterating over fixed length combinations
    of an input character set.

    Args:
        baseurl (str): entry point URL to base further connections off of.
        setchars (str): input character set to construct further sets from.
        setlength (int): length of the character set to output and generate.
        iteration (int): current iteration of the construction algorithm.
        enditeration (int): optional iteration to complete at.
        sleeptime (number): sleep time between requests to avoid spamming.
    '''

    totalsize = 0
    totalcount = 0

    # Number of characters in the character set.
    charcount = len(setchars)

    iteration_start = iteration
    iteration_max = int(enditeration) if enditeration else pow(charcount, setlength)

    # Get the current time for the timeout calculation.
    time_last = datetime.now()

    # Start iterating until we reach the max iterations.
    while iteration < iteration_max:
        # Skip iterations if we are catching up.
        if iteration < iteration_start:
            continue

        # Generate the current set.
        selection = generate(setchars, setlength, iteration)

        # Current iteration step.
        iteration = iteration + 1

        # Calculate the current time since the last loop.
        time_elapsed = (datetime.now() - time_last).total_seconds()

        # Check if enough time has past. Else, sleep until the time is up.
        if time_elapsed < sleeptime:
            time.sleep(sleeptime - time_elapsed)

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
