#More on files
#Python version 2.7

#Let's play a bit more with files and try to copy one file to another.

from sys import argv
from os.path import exists

script, filename_from, filename_to = argv #Expecting 2 pamaeters (plus script name)

print "Copying from %s to %s." % (filename_from, filename_to)

file_from = open(filename_from)
data_from = file_from.read() #Read all the content of the file til EOF

print "The input file is %d bytes long." % len(data_from)

#Check if the filename_to does exist locally in the working directory
print "Does the output file exist? %r" % exists(filename_to)
print "Ready, hit RETUR to continue. CTRL-C (^C) to abort."
raw_input("?")

file_to = open(filename_to, "w") #Need to write in the file
file_to.write(data_from)

print "Alright. All done!"

#Close all files
file_to.close()
file_from.close()

