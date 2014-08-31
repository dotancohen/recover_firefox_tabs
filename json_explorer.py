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

	while True:
		output_location(path, code)

	return True



def output_location(path, code):

	print('')
	print(' -> '.join(path))

	path_addition = []
	ordinal = 1
	current_element = code

	for p in path:
		current_element = current_element[p]

	for x in current_element:
		print('%2.0f: %s' % (ordinal, x,))
		path_addition.append(x)
		ordinal += 1

	while True:
		new_member = input('Select a new path member: ')

		if not new_member.isdigit():
			print('Please choose from the list')

		choosen = int(new_member)

		if choosen<0:
			print('Please enter a positive number!')
			continue

		if choosen==0:
			return path[:-1]

		if ordinal<choosen:
			print('Please choose from the list!')
			continue

		break

	return path.append(path_addition[choosen-1])



if __name__ == '__main__':

	if 1<len(sys.argv):
		filename = sys.argv[1]
	else:
		print('I need a file to work on!')
		sys.exit(-1)

	main(filename)
