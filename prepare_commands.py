#create a list of commands
#also associate a function to each command

import cPickle;
import marshal;
import types;
import sys;
import numpy;
import os;
import os.path;




"""Help function"""
def help():
 print "I will assist you..."





"""Look for"""
def look(inp):
 flag=0
 prev = []
 for p in inp:
  if p in tag_vs_files:
   if(tag_vs_files[p] not in prev):
    prev.append(tag_vs_files[p])
   flag=1
 if flag==1:
  prev = sum(prev,[])
  for temp in prev:
   print "::  ",temp
 else:
  print "No match found!"








"""Add tag of a file"""
def add(inp):
 if(len(inp)<2):
  print "Please specify tag followed by files"
  return
 tag = inp[0]
 if(tag not in tag_vs_files):
  tag_vs_files[tag]=[]
 files = inp[1:]
 for file in files:
  if(os.path.isfile(file)):
   tag_vs_files[tag].append(file)
  elif(os.path.exists(file)):
   for dirname, dirnames, filenames in os.walk(file):
    for filename in filenames:
     fname,extension = os.path.splitext(filename)
     filepath = os.path.join(file, filename)
     extension = extension[1:]
     if(extension not in tag_vs_files):
      tag_vs_files[extension]=[]
     tag_vs_files[extension].append(filepath)
     tag_vs_files[tag].append(filepath);
  else:
   print "No such file:",file
 outputfile = open('tag_vs_files_dictionary.pkl', 'wb')
 cPickle.dump(tag_vs_files, outputfile) 
 outputfile.close()
 












list = []
list.append(('help',marshal.dumps(help.func_code)))
list.append(('look',marshal.dumps(look.func_code)))
list.append(('add',marshal.dumps(add.func_code)))

myDict = dict(list)


outputfile = open('command_dictionary.pkl', 'wb')
cPickle.dump(myDict, outputfile)
outputfile.close()
