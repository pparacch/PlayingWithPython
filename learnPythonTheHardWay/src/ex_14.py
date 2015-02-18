#Prompting and Passing
#Python version 2.7

#Play with argv and raw_input to ask the user for something.

#argv
from sys import argv

script, user_name = argv #Unpack - we expect 2 arguments
prompt = "> "

print "Hi %s, I am the '%s' script" % (user_name, script)
print "I'd like to ask you a few questions."

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)

