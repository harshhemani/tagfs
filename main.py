import cPickle;
import marshal;
import types;
import sys;
import numpy;
import os.path, time
from subprocess import call

tag_vs_files_dictfile = 'tag_vs_files_dictionary.pkl'






"""
::: Something for pruning out the non-existing files :::
"""
def prune_filedict(dict):
 flag=0
 for (key,value) in dict.items():
  for filename in value:
   if(not os.path.isfile(filename)):
    value.remove(filename)
    print "---pruned file:",filename
    flag=1
    if(len(value)==0):
     del dict[key]
     print "--prune tag: ",key
     flag=1
 if(flag==1):
  print "++updated dictionary file"
  pkl_file = open(tag_vs_files_dictfile, 'wb')
  cPickle.dump(dict, pkl_file)
 return dict








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
           print "Internal Error, is your syntax correct?"
        elif(inp[0]=='quit' or inp[0]=='q'):
	 print "Exiting!"
         break;
	elif(inp[0]=='prune'):
	 tag_vs_files = prune_filedict(tag_vs_files);
        elif(inp[0]==''):
         continue
        else:
         print "Command not found!"
