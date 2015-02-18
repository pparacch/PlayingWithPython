#Functions car return something(s)
#Python version 2.7

#"return" can be used inside a function in order to return back sth to the caller
#some examples using some "calculation" functions

def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b #return the sum of a and b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a -b #return the difference  between a and b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b #return teh multiplcation between a and b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b #return the division between a and b

print "Let's do some math ..."
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle ..."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes:", what, "Can you do it by hand?"

