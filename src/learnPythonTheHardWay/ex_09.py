#More Printing, Printing, Printing
#Python version 2.7.4

#Here some new strange stuff!

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days #Note the space at the end of the 1st string
print "Here are the months: ", months

print "When using %r formatter to print a 'special' string"
print "Here are the months: %r" % months

print "When using %s formatter to print a 'special' string"
print "Here are the months: %s" % months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines of we want, or 5, or 6.
"""
