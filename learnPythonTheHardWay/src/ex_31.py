#Making Decision - playing around with if-elif-else statement
#Nested if-elif-else statement (be careful not a good practice))
#Python version 2.7

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ") #user is asked to select the door.

if door == "1":

	print "There is a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	action = raw_input("> ") #Wait for the user to make a decision

	if action == "1":
		print "The bear eats your face off. Good job! You are done!"
	elif action == "2":
		print "The bear eats your leg off. Good job! You are done!"
	else:
		print "Well, doing %s is problably better. Bear runs away." % action

elif door == "2":
	
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow Jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ") #Waiting for usr input
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	
	print "You stumble around and fall on a knife and die. Good job!"
