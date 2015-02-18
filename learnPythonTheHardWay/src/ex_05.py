#Still playing with Variables & Printing
#Python version 2.7.4

#Introducing a "format string"
#How to make string that have variables embedded in them.
# "This is a string with %d %s" % (3, "words")
# These are formatters
# %d - integer
# %s - string
# %r - whatever in raw format

my_name = "Pier Lorenzo Paracchini"
my_age = 43
my_height = 168 #cm
my_weight = 70 #kg
my_eyes = "Brown & Green"
my_teeth = "White"
my_hair = "Brown"

print "Let's tals about %s." % my_name
print "He is %d cm tall." % my_height
print "He is %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He has got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, watch out!
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "In the next line we will use just %r to enter the variables using a 'format string'"
print "%r, if I add %r, %r, and %r I get %r." % (my_name, my_age, my_height, my_weight, my_age + my_height + my_weight)

