# Unique Elements: Write a function that returns the unique elements in a list.

def unique_elements(lst):
	return list(set(lst))

print(unique_elements([1,2,1,4,1,6,3,6,6,7,3,9,2]))