#Reading Files
#Python version 2.7

#Another way to provide input to a script is to read from a file
#ex_15_sample.txt (example)

from sys import argv
script, file_name = argv #the file name is provided through the arguments

txt = open(file_name) #Open the file

print "Here is your file %r:" % file_name
print txt.read() #read is used ot read the content of the file

txt.close # Rememeber to close always a connection to file after using it

print "Type the filename again:"
file_name_again = raw_input("> ")

txt_again = open(file_name_again)
print txt_again.read()

txt_again.close()
