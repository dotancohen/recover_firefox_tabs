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
	try:
		input_file = open(filename, 'r')
	except Exception as e:
		print('I need a real file!')
		sys.exit(-1)

	try:
		code = json.loads(input_file.readline())
	except Exception as e:
		print('Not JSON!')
		sys.exit(-1)

	output_location(path, code)

	return True



def output_location(path, code):

	print(' -> '.join(path))

	ordinal = 1
	for x in code:
		print('%2.0f: %s' % (ordinal, x,))
		ordinal += 1

	new_member = input('Select a new path member: ')

	if new_member.isdigit():
		print('nice!' + str(new_member))
	else:
		print('I need a digit!')

	return path



if __name__ == '__main__':

	if 1<len(sys.argv):
		filename = sys.argv[1]
	else:
		print('I need a file to work on!')
		sys.exit(-1)

	main(filename)
