#!/usr/bin/env python
# Python version 3.4+

import sys
import os
import re
import math
import requests

# Simple ranged download script. For those times when the other end just decides
# to close the file stream and you end up with partial files. This fixes that issue.

# -> Requests is required. Use 'pip install requests' to download the module.

# This download script is partially extracted from my Bandcamp downloader, Campdown.

# The first argument is the url to download the file from.

# The second argument is the optional output folder the file should be written to.
# If none is specified the folder this script is in will be used.

# Check that this file's main function is not being called from another file.
if __name__ == "__main__":
	try:
		# Fetch the program arguments and make sure that they are valid.
		try:
			url = sys.argv[1].replace('"', '')

		except:
			print('\nMissing required URL argument')
			sys.exit(2)

		if not "http://" in url and not "https://" in url:
			print('\n%s is not a valid URL' % url)
			sys.exit(2)

		# Get the path of the current execution folder.
		folder = os.path.split(os.path.abspath(__file__).replace('\\', '/'))[0] + "/"
		name = re.findall('(?=\w+\.\w{3,4}$).+', url)[0]

		# Get the size of the remote file.
		full_response = requests.get(url, stream = True)
		total_length = full_response.headers.get('content-length')

		# Open a file stream which will be used to save the output string
		with open(folder + "/" + re.sub('[\\/:*?<>|]', "", name), "wb") as f:
			# Make sure that the printed string is compatible with the user's command line. Else, encode.
			# This applies to all other print arguments throughout this file.
			try:
				print('Downloading: %s' % name)
				
			except UnicodeEncodeError:
				try:
					print('Downloading: %s' % name.encode(sys.stdout.encoding, errors = "replace").decode())

				except UnicodeDecodeError:
					print('Downloading: %s' % name.encode(sys.stdout.encoding, errors = "replace"))

			# If the file is empty simply write out the returned content from the request.
			if total_length is None:
				f.write(full_response.content)

			else:
				# Storage variables used while evaluating the already downloaded data.
				dl = 0
				total_length = int(total_length)
				cleaned_length = int((total_length * 100) / pow(1024, 2)) / 100
				block_size = 2048

				for i in range(math.ceil(total_length / 1048576)):
					response = requests.get(url, headers = {'Range': 'bytes=' + str(i * 1048576) + "-" + str((i + 1) * (1048576) - 1)}, stream = True)

					for chunk in response.iter_content(chunk_size = block_size):
						# Add the length of the chunk to the download size and write the chunk to the file.
						dl += len(chunk)
						f.write(chunk)

						# Display a loading bar based on the currently download filesize.
						done = int(50 * dl / total_length)
						sys.stdout.write("\r[%s%s%s] %sMB / %sMB " % ('=' * done, ">", ' ' * (50 - done), (int(((dl) * 100) / pow(1024, 2)) / 100), cleaned_length))
						sys.stdout.flush()

		# Insert a new line for formatting-OCD's sake.
		print('\n')

	except (KeyboardInterrupt):
		print("Interrupt caught - exiting program...")
		sys.exit(2)