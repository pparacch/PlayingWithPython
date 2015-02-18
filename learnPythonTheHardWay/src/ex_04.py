#Variables & Names
#Playing around with variables, assignments and basic calculations.

#Python version 2.7.4

cars = 100 #assign to (variable) car the value 100 (integer)
space_in_a_car = 4.0 #assign to (variable) space_in_a_car teh value 4.0 (floating point)
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car #Note! Multiplcation integer by float
average_passengers_per_car = passengers / cars_driven #Note! Division between integres -> integer

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need ot put about", average_passengers_per_car, "in each car."

