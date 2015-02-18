#Names, Variables, Code & Functions
#Python version 2.7

#Functions:
# 1. name peices of code (same as variables)
# 2. take arguments
# 3. create mini-scripts or tiny-commands

#Function
# def keyword
# indentation is key


#different examples of functions printing out 2 (passed) arguments
#Here is a special syntax to pass arguments '*args' -it behaves like argv but for functions
def print_two(*args):
	arg1, arg2 = args #behave like argv
	print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#a function expectinag and printing one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#Function with No arguments
def print_none():
	print "I got nothing."


print_two("Pier Lorenzo", "Paracchini")
print_two_again("Speedy", "Gonzales")

print_one("Flinstons")

print_none()
	 
