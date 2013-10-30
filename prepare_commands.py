#create a list of commands
#also associate a function to each command

import cPickle;
import marshal;
import types;
import sys;
import numpy;
import os;
import os.path;
from subprocess import call



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
  prev = set(sum(prev,[]))
  for temp in prev:
   print "::  ",temp
 else:
  print "No match found!"


"""intersection"""
def intersection(inp):
 flag=0
 set1 = set()
 for p in inp:
  if p in tag_vs_files:
   if(flag==0):
    set1 = set(tag_vs_files[p])
    flag=1
   else:
    set1 = set1 & set(tag_vs_files[p])
  else:
   print "One or more tags that you mentioned, do not exist!"
   print "+exception tag: ",p
   return 
 if(len(set1)==0):
  print "NULL SET"
 else:
  for item in set1:
   print ":: ",item







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
   fname,extension = os.path.splitext(file)
   extension = extension[1:].strip()
   if(extension!=''):
    if(extension not in tag_vs_files):
     tag_vs_files[extension]=[]
    if(file not in tag_vs_files[extension]):
     tag_vs_files[extension].append(file)
   file = os.path.abspath(file)
   if(file not in tag_vs_files[tag]):
    tag_vs_files[tag].append(file)
   print "Added: ",file,"with tag: ",tag
  elif(os.path.exists(file)):
   for dirname, dirnames, filenames in os.walk(file):
    for filename in filenames:
     fname,extension = os.path.splitext(filename)
     filepath = os.path.join(dirname, filename)
     #print "~",dirname, dirnames, filename
     filepath = os.path.abspath(filepath)
     extension = extension[1:].strip()
     if(extension!=''):
      if(extension not in tag_vs_files):
       tag_vs_files[extension]=[]
      if(filepath not in tag_vs_files[extension]):
       tag_vs_files[extension].append(filepath)
     if(filepath not in tag_vs_files[tag]):
      tag_vs_files[tag].append(filepath)
     print "Added: ",filepath,"with tag: ",tag
  else:
   print "No such file:",file
 outputfile = open('tag_vs_files_dictionary.pkl', 'wb')
 cPickle.dump(tag_vs_files, outputfile) 
 outputfile.close()
 



"""System calls"""
def sys_call(inp):
 try:
  call(inp)
 except:
  print "Hmmm, something seems to be wrong here.."


"""STATS"""
def stat():
 print "Tag count: ",len(tag_vs_files)
 print "File count: ",len(set(sum(tag_vs_files.values(),[])))
 





list = []
list.append(('help',marshal.dumps(help.func_code)))
list.append(('l',marshal.dumps(look.func_code)))
list.append(('U',marshal.dumps(look.func_code)))
list.append(('isect',marshal.dumps(intersection.func_code)))
list.append(('I',marshal.dumps(intersection.func_code)))
list.append(('add',marshal.dumps(add.func_code)))
list.append(('sys',marshal.dumps(sys_call.func_code)))
list.append(('!',marshal.dumps(sys_call.func_code)))
list.append(('stats',marshal.dumps(stat.func_code)))


myDict = dict(list)


outputfile = open('command_dictionary.pkl', 'wb')
cPickle.dump(myDict, outputfile)
outputfile.close()
