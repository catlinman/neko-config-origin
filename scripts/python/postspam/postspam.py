#!/usr/bin/env python
# Python version 3.4+

"""Postspam
Usage:
    postspam.py <URL> <DATA>
                [--count=COUNT]
                [--sleep=SLEEP]
                [--random=RANDOM]
    postspam.py (-h | --help)
    postspam.py (-v | --version)

Options:
    -h --help           Show this screen.
    -v --version        Show version.

    -u --url=<URL>          Entry point URL to use.
    -d --data=<DATA>        Input data CSV file to work with.

    -c --count<COUNT>       Total amount of requests to make.
    -s --sleep<SLEEP>       Optional time between requests to sleep.
    -r --random<RANDOM>     Percentage of sleep time to randomly select from.

Description:
    Makes POST requests to a given URL with randomized field selection data
    from an input CSV file. CSV headers determine the fields to set.

Requirements:
    Python 3.4+, requests, docopt
"""

# Import basic modules.
import os
import time
import csv
import random

# Import additionall modules.
import requests

from docopt import docopt


def loadcsv(filename):
    '''
    Reads an input CSV file.

    Args:
        filename (str): input file path.

    Returns:
        List containing all rows from the CSV file without headers.
    '''

    with open(filename, "r", encoding="utf-8") as f:
        return list(filter(None, list(csv.reader(f))[1:]))


def cli():
    args = docopt(__doc__, version="Postspam 0.1")
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Handle arguments.
    url = args["<URL>"]
    datapath = args["<DATA>"]

    # Handle optional arguments.
    count = int(args["--count"]) if args["--count"] else 1
    sleep = int(args["--sleep"]) if args["--sleep"] else 1
    rand = float(args["--random"]) if args["--random"] else 1

    if os.path.isfile(datapath):
        data = loadcsv(datapath)

    else:
        print("The specified data file does not exist.")
        return

    # Prepare headers.
    headers = requests.utils.default_headers()

    headers.update = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept-Encoding": ", ".join(("gzip", "deflate")),
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

    iteration = 0  # Iterator.

    while iteration < count:
        # Payload data container.
        payload = {}

        # Iterate over our data and start inserting random selections as the payload.
        for row in data:
            key = row[0]  # Get they key and pop it from the row.

            # If the key already exists we combine the new data with the already present data.
            if key in payload:
                payload[key] = "{} {}".format(payload[key], random.choice(row[1:]).strip())

            # If not add a new key to the dictionary. Also make sure to strip whitespace.
            else:
                payload[key] = random.choice(row[1:]).strip()

        # Print some status information to the console.
        print("Current payload data:")

        for key, value in payload.items():
            print("{} = {}".format(key, value))

        # Make a request with our designated settings.
        r = requests.post(url, headers=headers, data=payload)

        # Handle possible errors.
        if(r.status_code != 200):
            print("An error occured during the request. Status code {}.".format(r.status_code))

        # Increment the count.
        iteration += 1

        # Make sure to sleep the program if we haven't reached the maximum iteration.
        if(iteration < count):
            sleepnow = random.randint(sleep * rand, sleep)

            print("Sleeping for {} seconds...".format(sleepnow))

            time.sleep(sleepnow)

    print("Finished spamming. You should be ashamed.")


# Main program entry point.
if __name__ == "__main__":
    cli()
