#More pRactice - gluing all together
#Python version 2.7

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs.'

poem = """\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is one."""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five:", str(five)

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 10
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of %r" % start_point
print "We'd have %d beans, %d jars and %d crates." % (beans, jars, crates)

start_point = start_point / 10
print "We can also do that this way."
print "We'd have %d beans, %d jars and %d crates." % secret_formula(start_point)




