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
		path = output_location(path, code)

	return True



def output_location(path, code):

	nozero = False
	ordinal = 1
	path_addition = []
	current_element = code

	print('')

	if len(path)==0:
		print('Top level!')
		nozero = True
	else:
		print(' -> '.join(path))
		print('%2.0f: %s' % (0, 'Up one level.',))

	for p in path:
		current_element = current_element[p]

	for ce in current_element:
		ce_type = str(type(current_element[ce]))
		ce_type = ce_type[ce_type.find("'")+1:]
		ce_type = ce_type[:ce_type.find("'")]
		print('%2.0f: %s (%s)' % (ordinal, ce, ce_type,))
		path_addition.append(ce)
		ordinal += 1

	while True:
		new_member = input('Select a new path member: ')

		if not new_member.isdigit():
			print('Please choose from the list')
			continue

		choosen = int(new_member)

		if choosen<0:
			print('Please enter a positive number!')
			continue

		if choosen==0:
			if nozero:
				print('Please choose from the list')
				continue

			return path[:-1]

		if ordinal<choosen:
			print('Please choose from the list!')
			continue

		break

	path.append(path_addition[choosen-1])
	return path



if __name__ == '__main__':

	if 1<len(sys.argv):
		filename = sys.argv[1]
	else:
		print('I need a file to work on!')
		sys.exit(-1)

	main(filename)
