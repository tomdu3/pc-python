# Dictionary Merger: Write a function that merges two dictionaries. If there is a conflict between dictionaries (same key), the value from the second dictionary should be kept.

def merge_dictionaries(dict1, dict2):
	merged_dict = dict1.copy()
	merged_dict.update(dict2)
	return merged_dict

dict1 = {
	'name': 'Tom',
	'age': 43,
	'occupation': 'software developer',
}

dict2 = {
	'name': 'Mark',
	'age': 23,
	'hobby': 'music composer',
}

print(merge_dictionaries(dict1, dict2))