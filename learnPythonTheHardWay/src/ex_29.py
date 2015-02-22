#What If - start to play with if statement (compound statement)
#Python version 2.7

people = 20
cats = 30
dogs = 15

print "people: %d, cats: %d, dogs: %d\n" % (people, cats, dogs)

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

print "\npeople: %d, cats: %d, dogs: %d\n" % (people, cats, dogs)

if people >= dogs:
	print "people are greater than or equal to dogs."

if people <= dogs:
	print "people are less than or equal to dogs."

if people == dogs:
	print "people are dogs."
