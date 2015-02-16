#More Practice with functions & variables - putting all together
#Python version 2.7

def break_words(stuff, sep = " "):
	"""This function breaks up words for us."""
	words = stuff.split(sep)
	return words

def sort_words(words):
	"""Sort the words alphabetically."""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Print out the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Take in a full sentence and return the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and last words in teh sentence."""
	words = break_words(sentence)
	print first_word(words)
	print last_word(words)

def print_and_last_sorted(sentence):
	"""Sort the words and then prints teh first and last."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


