#!/usr/bin/env python
# Python version 3.4+

import os
import sys
import datetime

name = "datewrite.txt"  # Output filename.

# Check that this file's main function is not being called from another file.
if __name__ == "__main__":
    try:
        # Get the path to write to.
        output_folder = sys.argv[1]

    except(IndexError):
        output_folder = ""

    # Get the script path in case no output path is specified.
    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '')

    if output_folder:
        # Make sure that the output folder has the right path syntax
        if not os.path.isabs(output_folder):
            if not os.path.exists(os.path.join(script_path, output_folder)):
                os.makedirs(os.path.join(script_path, output_folder))

            output = os.path.join(script_path, output_folder)

    else:
        # If no path is specified use the absolute path of the main file.
        output_folder = script_path

    # Get the current time.
    date = datetime.datetime.now()

    # Open a new file or append to an already existing file.
    f = open("{}/{}".format(output_folder, name), "a")

    # Write the header if the selected file is empty.
    if not os.path.getsize(os.path.join(output_folder, name)) > 0:
        f.write("- Time and date register -\n\n")
    else:
        f.write("\n\n")

    # Write the current time data to the file and close it afterwards.
    f.write("Date: {}.{}.{}\nTime: {}:{}\nSeconds: {}\nMicroseconds: {}".format(
        date.day, date.month, date.year, date.hour, date.minute, date.second, date.microsecond))
    f.close()
