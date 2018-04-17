import pickle, os

def replaceNames(directory):

	directories = []

	# Scan through datafolders in directory
	for folder in os.listdir(directory):
		# Scan through files in each folder
		for file in os.listdir( os.path.join(directory, folder) ):
			# Search for info files
			if file.endswith('Information.pickle'):

				# Load infofile
				with open(os.path.join(directory, folder, file), "rb") as input:
					file_info  = pickle.load(input)

				# Replace directory with the correct one
				file_info.data_path = directory
				# Replace photo_path with the directory name
				file_info.photo_path = os.path.join(directory,folder)
				
				# Repickle file
				file_info.pickleInformation(file)

				directories.append(os.path.join(directory, folder, file))

	print("New data_path ("+directory+") set for the following files : ")
	for file in directories: print(file)


if __name__ == '__main__':

	directory = raw_input("Location of data directory: ")

	replaceNames(directory)