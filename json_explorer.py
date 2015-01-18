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

	for p in path:
		if type(current_element)==type([]):
			p = int(p)
		current_element = current_element[p]

	if len(path)==0:
		print('Top level!')
		onTopLevel = True
	else:
		print(' -> '.join(path) + ' ' + str(type(current_element)))

	if type(current_element)==type(42):
		print("Int Value: %i" % (current_element,))
		return path[:-1]

	if type(current_element)==type('hello'):
		print("Str Value: %s" % (current_element,))
		return path[:-1]

	if type(current_element)==type({'adam':'eve'}):
		for index, ce_sub in enumerate(current_element):
			if type(ce_sub)==type([]):
				ce_sub_type = str(type(current_element[index]))
			else:
				ce_sub_type = str(type(current_element[ce_sub]))
			ce_sub_type = ce_sub_type[ce_sub_type.find("'")+1:]
			ce_sub_type = ce_sub_type[:ce_sub_type.find("'")]

			# Types observered: dict lit int

			if ce_sub_type in ['dict', 'list']:
				ce_sub_type += ' ' + str(len(current_element[ce_sub]))

			if ce_sub_type == 'str':
				ce_sub_type += ' ' + ce_sub[:50]
				if len(ce_sub)>50:
					ce_sub_type += '...'

			if ce_sub_type == 'int':
				ce_sub_type += ' ' + str(current_element[ce_sub])

			print('%2.0f: %s (%s)' % (ordinal, ce_sub, ce_sub_type,))
			path_addition.append(ce_sub)
			ordinal += 1

	if not onTopLevel:
		print('%2.0f: %s' % (0, 'Up one level.',))

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

		if ordinal<=choosen:
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
