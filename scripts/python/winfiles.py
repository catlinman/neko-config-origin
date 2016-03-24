#!/usr/bin/env python
# Python version 3.5+

import os
import sys
import re
import datetime

# Iterates over a directory and makes filenames safe for transfer to Windows based
# filesystems. Removes illegal characters and also gets rid of junk files such as
# the well known .DS_Store files. Also writes an output log file in the given
# directory which can be checked and used to reverse changes. This would required
# an extra script though.


def make_safe(string):
    return re.sub('[:*?<>|]', "", string).replace("/", "").replace("\\", "")

if __name__ == "__main__":
    dircount = 0
    filecount = 0
    removecount = 0

    removelist = [".DS_Store"]

    changes = []

    try:
        search_dir = sys.argv[1]

    except(IndexError):
        search_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "")

    for subdir, dirs, files in os.walk(search_dir):
        for f in files:
            if f in removelist:
                print("R {}".format(os.path.join(subdir, f)))

                os.remove(os.path.join(subdir, f))

                removecount += 1
                continue

            new = make_safe(f)

            if f != new:
                formatted = "F {} >> {}".format(f, new)
                changes.append(formatted)

                print(formatted)

                os.rename(os.path.join(subdir, f), os.path.join(subdir, new))

                filecount += 1

        for d in dirs:
            new = make_safe(d)

            if d != new:
                formatted = "D {} >> {}".format(d, new)
                changes.append(formatted)

                print(formatted)

                os.rename(os.path.join(subdir, d), os.path.join(subdir, new))

                dircount += 1

    print("Renamed a total of {} directories and {} files. Removed {} junk files.".format(
        dircount, filecount, removecount))

    print("Writing log to '{}'".format(
        os.path.join(search_dir, 'winfiles_log.txt')))

    log = open(os.path.join(search_dir, 'winfiles_log.txt'), 'a')
    log.write("Winfiles converter script log written at {}\n".format(
        str(datetime.datetime.now())))

    log.write("Renamed a total of {} directories and {} files. Removed {} junk files.\n".format(
        dircount, filecount, removecount))

    for line in changes:
        log.write("{}\n".format(line))

    log.write("\n\n")
    log.close()
