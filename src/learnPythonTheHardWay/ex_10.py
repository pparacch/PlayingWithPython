#Play with strings & special formatting characters (escape characters)
#Python version 2.7

#Common escape characters
#\\ backslash
#\' single quote
#\" double quote
#\a ascii bell
#\b ascii backspace
#\n ascii line feed
# ...

#Please note! When using %r in string formats - escape characters are not resolved.


tabby_cat = "\tI'm tabbed in." #\t -> tab char
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print "\nA funny piece of code to run:\n"

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,

