#Reading and Writing Files
#Python version 2.7

#Playing with some important methods of files like
#close
#read
#readline
#truncate
#write(stuff)

from sys import argv

#Use test.txt as filename - and to run this script.
script, filename = argv

print "We are going to erase %r." % filename
print "If you do not want that, hit CRTL-C (^C)."
print "if you want that, hit RETURN."

raw_input("?")

print "Opening the file ..."
target = open(filename, "w") 

#Open the file (filename) with "w" (write) rights
#by default a file is open with "r" (reading) rights.

print "Truncating the file. Goodbye!!"
target.truncate() #Remove all of the content in the file

print "Now I'm going to ask you for three lines."

line_1 = raw_input("line 1: ")
line_2 = raw_input("line 2: ")
line_3 = raw_input("line 3: ")

print "I am going to write these lines to the file."

target.write(line_1)
target.write("\n")

target.write(line_2)
target.write("\n")

target.write(line_3)
target.write("\n")

print "And finally, we close the file."
target.close() #Always remember to close a file when done.



