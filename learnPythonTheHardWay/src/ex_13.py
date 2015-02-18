#Parameters, Unpacking and Variables
#Python version 2.7

#Learn how to pass parameter(s) to the Python script

#import - a way to add features to the script from other modules.
#argv is the argument variable. It holds the arguments you pass to the Python script when
#you run it.

from sys import argv

#The next line of code unpacks argv - assigning the arguments to the 3 variables.
##Expected script name (default) + 3 extra parameters 
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "Type of arguments: %r, %r, %r" % (type(first), type(second), type(third))

#Outcome
#If you do not pass enough arguments - an error is triggered
#If you do pass more than 3 arguments - an error is triggered
#All arguments passed are treated as strings
#If you need to pass number - use int() or float() to convert them.
