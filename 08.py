# List Flattener: Develop a function that takes a list of lists and flattens it to a single list without using any built-in Python flattening functions.

def flatten_list(nested_list):
	flat_list = []
	for element in nested_list:
		if isinstance(element, list):
			flat_list.extend(flatten_list(element))
		else:
			flat_list.append(element)
	return flat_list

print(flatten_list([0,1,2,[3,4,[5,6],7,8],9]))