#Functions & Files
#Python version 2.7

#How files and functions can play together

from sys import argv

#get the script name and filename from argv
script, filename = argv

#print out all of the content of the file
def print_all(f):
	print f.read()

#rewind the current position within the file at the beginning of the file
def rewind(f):
	f.seek(0)

#print out a line form the file with teh provided line counter
def print_a_line(line_count, f):
	#Note!! the readline() finction return the "\n" that's in the file at the end of the line
	print line_count, f.readline(), #"," to remove the "\n" added by print funtion
	#readline() -the file f is responsible for maintaining the current position in the file
	#after each operations performend on teh file itself.

#Let's open a file - e.g. test.txt
current_file = open(filename)

print "First let's print out the whole file:\n"
print_all(current_file)

print "Now let's rewind the file (like a tape) ..."
rewind(current_file)

print "And now let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 11
print_a_line(current_line, current_file)
