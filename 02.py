# Palindrome Checker: Create a function that checks if a given string is a palindrome (reads the same backward as forward, ignoring spaces, punctuation, and capitalization).

def is_palindrome(s):
	clean_str = s.replace('', '').lower()
	clean_str = ''.join([char for char in clean_str if char.isalnum()])
	print(clean_str)
	return clean_str == clean_str[::-1]

text = 'Rev.er'
if (is_palindrome(text)):
	print(f'{text} is a palindrome!')
else:
	print (f'{text} is not a palindrome!')
