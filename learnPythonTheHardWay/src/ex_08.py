#More Printing Printing
#Python version 2.7.4

#Playing with "format string" :)

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (True, False, False, True)

print "formatter applied for the next string format is %r" % formatter
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

#By default when using %r strings are printed out with single quotes. Double quotes are used
#when single quotes are used inside.

new_formatter = "%s %s %s %s"
print "formatter applied for the next string format is %r" % new_formatter
print new_formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
