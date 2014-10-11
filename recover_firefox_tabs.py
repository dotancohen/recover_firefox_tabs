#!/usr/bin/python3

"""

Application to restore Firefox tabs when Firefox forgets a session.

TODO
----
Support non-Linux operating systems

"""

import json
import os
import sys



def main(argv):

	if len(argv)>1:
		search_location = argv[1]
	else:
		search_location = os.getcwd() + '/.mozilla/'

	session_file_canonical_name = 'sessionstore.bak'
	base_directory_for_recovered_files = os.getcwd()

	session_files = getFirefoxSessionFiles(search_location, session_file_canonical_name)

	if len(session_files)==0:
		print("No Firefox profiles found.")
		return False

	for session_file in session_files:
		recovered_name = getValidRecoveredName(base_directory_for_recovered_files)
		recoverSessionTabs(session_file, recovered_name)

	return True



def getFirefoxSessionFiles(search_location, session_file_canonical_name):

	session_files = []

	if os.path.isfile(search_location):
		return [search_location]

	for dirName, dirs, files in os.walk(search_location):
		if session_file_canonical_name in files:
			session_files.append(dirName + '/' + session_file_canonical_name)

	return session_files



def getValidRecoveredName(base_directory):

	base_name = 'recovered_tabs'
	base_extension = '.html'

	if not base_directory.endswith('/'):
		base_directory += '/'

	name_number = 0
	tries = 10
	number_representation = ''

	while name_number<=tries:

		if 0<name_number:
			number_representation = '_' + str(name_number)

		filename = base_directory + base_name + number_representation + base_extension

		if not os.path.isfile(filename):
			break

		name_number += 1

	return filename



def recoverSessionTabs(session_file, recovered_name):

	# $ file -i sessionstore.bak
	# sessionstore.bak: text/html; charset=utf-8

	input_file = open(session_file, 'r', encoding='UTF-8')
	output_file = open(recovered_name, 'w', encoding='UTF-8')

	code = json.loads(input_file.readline())
	found_urls = []
	output_format = '<li><a href="%s">%s</a></li>'

	output_file.write("""
	<html><head>
		<title>Recovered Firefox Tabs</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	</head><body>
		<h1>Recovered Firefox Tabs</h1>
		<ol>
	""")

	for tab in code['_closedWindows'][0]['tabs']:
	#for tab in code['windows'][0]['tabs']:
		url = tab['entries'][-1]['url']
		if not url in found_urls:
			found_urls.append(url)
			title = tab['entries'][-1]['title']
			output_file.write(output_format % (url, title, ))


	output_file.write("""
		</ol>
	</body></html>
	""")

	return True



if __name__ == '__main__':
	main(sys.argv)
