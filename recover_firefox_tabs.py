#!/usr/bin/python3

"""

Application to restore Firefox tabs when Firefox forgets a session.

"""

import os



def main():

	mozilla_directory = os.getcwd() + '/.mozilla/'
	session_file_canonical_name = 'sessionstore.bak'
	base_directory_for_recovered_files = os.getcwd()

	session_files = getFirefoxSessionFiles(mozilla_directory, session_file_canonical_name)

	for session_file in session_files:
		recovered_name = getValidRecoveredName(base_directory_for_recovered_files)
		recoverSessionTabs(session_file, recovered_name)

	return True



def getFirefoxSessionFiles(mozilla_directory, session_file_canonical_name):

	session_files = []

	for dirName, dirs, files in os.walk(mozilla_directory):
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

	# TODO
	print(session_file + ' ' + recovered_name)

	return True



if __name__ == '__main__':
	main()
