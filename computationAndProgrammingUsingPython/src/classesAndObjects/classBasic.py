#Basic concepts behind classes and objects
#Python version 2.7

#Create a new class - class statement is used
#class tells Python that this is a new class

#Between brackets other classes name can be passed (e.g by default object should be passed) - inheritance
class Coordinate(object):

	"""A constructor can be provided in order to give initial values to teh attibutes
	of the class when instantiating a class.""" 

	#The constructor: this method is called when an object is created.

	"""An object's attributes are variables that can be used be used throughout the entire object, regardless of the method in which it is first defined. 
	However, it is customary to define attributes within the __init__ method for many reasons. Primarily this is to ensure all attributes are properly initialized.
	Because the __init__ method is called when an object is created, if a  number
	attributes are created in the __init__ method they will be initialized properly
	(and thus not throw any errors) when they are referenced later on."""

	def __init__(self, x, y):
		#self -> convention teh first attribute is "self" (could be called in another way) - a pointer to the instance of teh class itself
		self.x = x #create x in self and initialize it (bind x to the instance)
		self.y = y #create y in self and initialize it (bind y to teh instance)


#How to use the class that we have just created
c = Coordinate(3,4) #create a new instance c
origin = Coordinate(0, 0) #create a new instance origing

#Note! those are two different instances 

print c.x, c.y
print origin.x, origin.y 
