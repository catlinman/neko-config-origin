#!/usr/bin/env python
# Python version 3.4+

import os
import sys
import datetime

# Check that this file's main function is not being called from another file.
if __name__ == "__main__":
	try:
		# Make sure that the output folder has the right path syntax
		outputfolder = sys.argv[1].replace('\\', '/')

		# Check if the path is relative or absolute. If relative, make it absolute.
		if outputfolder[-1] != "/": outputfolder = str(outputfolder) + "/"
		
		if not os.path.isabs(outputfolder):
			if not os.path.exists(os.path.split(os.path.abspath(__file__).replace('\\', '/'))[0] + "/" + outputfolder):
				os.makedirs(os.path.split(os.path.abspath(__file__).replace('\\', '/'))[0] + "/" + outputfolder);

			outputfolder = os.path.split(os.path.abspath(__file__).replace('\\', '/'))[0] + "/" + outputfolder

	except:
		# If no path is specified revert to the absolute path of the main file.
		outputfolder = os.path.split(os.path.abspath(__file__).replace('\\', '/'))[0] + "/"

	try:
		# Get the filename to write to.
		filename = sys.argv[2].replace('"', '')

	except:
		# Write to the default filename of datewrite.txt
		filename = "dreg.txt"

	# Get the current time.
	date = datetime.datetime.now()

	# Open a new file or append to an already existing file.
	f = open("%s/%s" % (outputfolder, filename), "a")

	# Write the header if the selected file is empty.
	if not os.path.getsize("%s/%s" % (outputfolder, filename)) > 0: f.write("- Time and date register -\n\n")
	else: f.write("\n\n")

	# Write the current time data to the file and close it afterwards.
	f.write("Date: %s.%s.%s\nTime: %s:%s\nSeconds: %s\nMicroseconds: %s" % (date.day, date.month, date.year, date.hour, date.minute, date.second, date.microsecond))
	f.close()