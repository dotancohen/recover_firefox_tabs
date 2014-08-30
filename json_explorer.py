#!/usr/bin/python3

"""

Application to explore JSON files to learn their format.

TODO
----
Support non-Linux operating systems

"""

import json
import os
import sys



def main(filename):

	path = []
	input_file = open(filename, 'r')
	code = json.loads(input_file.readline())

	for x in code:
		print(x)

	return True



if __name__ == '__main__':

	if 1<len(sys.argv):
		filename = sys.argv[1]
	else:
		print('I need a file to work on!')
		sys.exit(-1)

	main(filename)
