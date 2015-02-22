#Else and if - play with if-elif-else statement (compound statement)
#branching based on some boolean conditions (see examples below)
#the block of code that is actually run depends on the boolean conditions.
#Note! If servral boolean conditions are Ture (part of teh same if-elif-else statement)
#only the first valid (True) boolean conditionis run.

#Python version 2.7

people = 30
cars = 40
buses = 15

print "\npeople: %d, cars: %d, buses: %d\n" % (people, cars, buses)

print "\ncars > people: %s" % (cars > people)
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We shoudl not take the cars."
else:
	print "We can't decide"


print "\nbuses > cars: %s" % (buses > cars)
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still cannot decide."

print "\npeople >buses: %s" % (people > buses)
if people > buses:
	print "Alright let's just take the buses."
else:
	print "Fine, let's stay home then."

