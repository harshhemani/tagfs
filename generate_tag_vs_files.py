import cPickle;
import os;

target_directory = "sample/"

dictionary = dict()

for dirname, dirnames, filenames in os.walk(target_directory):
    # print path to all filenames.
    for filename in filenames:
        fname,extension = os.path.splitext(filename)
	extension = extension[1:]
        filepath = os.path.join(dirname, filename)
	if(extension not in dictionary):
		dictionary[extension]=[]
	dictionary[extension].append(filepath)
outputfile = open('tag_vs_files_dictionary.pkl', 'wb')
cPickle.dump(dictionary, outputfile)
