#Strings & Text
#Python version 2.7.4

#A string in general is a bit of text that you want to disply to someone or "export2
#out of the program. String can be set using "" (double quotes) or '' (single quotes)
#around the text.

#'print' function is used to print out string(s) or "format string".

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who knows %s and whose who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x #using %r formatter (raw)
print "I also said: '%s'" % y #using %s formatter (string)

hilarious = False #Boolean
joke_evaluation = "Isn't that joke funny!? %r"

print joke_evaluation % hilarious

w = "This is the left side of ... "
e = "a string with a right side."

print w + e #concatenation of two string 
