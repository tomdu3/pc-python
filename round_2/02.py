# Anagram Checker: Create a function that checks whether two strings are anagrams of each other.
# Hint: Use a dictionary to count the occurrences of each character in both strings and then compare.

def anagram_checker(string1, string2):
	dict1 = str_to_dict(string1.lower())
	dict2 = str_to_dict(string2.lower())

	if dict1.keys() != dict2.keys():
		return False
	else:
		for key in dict1.keys():
			if dict1[key] != dict2[key]:
				return False
		return True


def str_to_dict(string):
	dict = {}
	for char in string:
		if char not in dict:
			dict[char] = 1
		else:
			dict[char] += 1
	return dict


print(anagram_checker('ana', 'NaA'))