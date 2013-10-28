import cPickle;
import marshal;
import types;
import sys;
import numpy;
import os.path, time

tag_vs_files_dictfile = 'tag_vs_files_dictionary.pkl'

#read tag_vs_files dictionary
pkl_file = open(tag_vs_files_dictfile, 'rb')
tag_vs_files = cPickle.load(pkl_file)

#read command dictionary
pkl_file = open('command_dictionary.pkl', 'rb')
commands = cPickle.load(pkl_file)


#read user commands
while(True):
	inp = raw_input('tagfs#: ')
	inp = inp.strip()
	inp = inp.split(' ');
        if(inp[0] in commands):
	 func = types.FunctionType(marshal.loads(commands[inp[0]]), globals(), "something")
         try:
          if(len(inp)>1):
           func(inp[1:])
          else:
	   func()
         except:
           print "incorrect format, try looking the correct format in help"
	   raise
        elif(inp[0]=='quit' or inp[0]=='q'):
	 print "Exiting!"
         break;
        else:
         print "Command not found!"
