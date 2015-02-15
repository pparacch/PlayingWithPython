#Functions & Variables
#Python version 2.7

#Play around with a function -passing the variables in different ways

#function used to play general info about cheese and cracker status for the party
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses." % cheese_count
	print "you have %d boxes of crackers." % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly."
cheese_and_crackers(20, 30) #call the function passing directly the amount of cheese and crackers

print "Or, we can use variables ..."
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)#call the function using variables

print "We can even do math inside ...."
cheese_and_crackers(10 + 20, 5 + 6)#call the function doing some math with numbers

print "And we can combine the two, variables and math ..."
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)#call the funtion doing some math with numbers & variables 

