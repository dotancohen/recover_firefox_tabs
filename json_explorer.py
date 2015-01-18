#!/usr/bin/python3

"""

Application to explore JSON files

TODO

* Support non-Linux operating systems
* Add search feature
* Recursive tree view (display entire format N nodes deep)



KNOWN ISSUES

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

	"""
	path: list
	code: json

	returns list
	"""

	onTopLevel = False
	ordinal = 1
	path_addition = []
	current_element = code

	print('')

	if len(path)==0:
		print('Top level!')
		onTopLevel = True
	else:
		print(' -> '.join(path))
		print('%2.0f: %s' % (0, 'Up one level.',))

	for p in path:
		current_element = current_element[p]

	for ce_sub in current_element:
		ce_sub_type = str(type(current_element[ce_sub]))
		ce_sub_type = ce_sub_type[ce_sub_type.find("'")+1:]
		ce_sub_type = ce_sub_type[:ce_sub_type.find("'")]

		# Types observered: dict lit int

		if ce_sub_type in ['dict', 'list']:
			ce_sub_type += ' ' + str(len(current_element[ce_sub]))

		print('%2.0f: %s (%s)' % (ordinal, ce_sub, ce_sub_type,))
		path_addition.append(ce_sub)
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
			if onTopLevel:
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
