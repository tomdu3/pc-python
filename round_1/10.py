# String Reverser: Create a function that takes a string and returns the string in reversed order without using the [::-1] syntax.

def reverse_string(s):
	reversed_str = ''
	for i in range(len(s)):
		reversed_str += s[len(s)-i-1]
	return reversed_str

print(reverse_string('Tomislav'))