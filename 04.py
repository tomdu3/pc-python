def frequency_counter(numbers):
	frequency = {}
	# Loop over numbers and popullate the frequency dictionary
	for number in numbers:
		if number in frequency:
			frequency[number] += 1
		else:
			frequency[number] = 1
	return frequency


print(frequency_counter([1,1,2,2,2,3333,33,3,3,100,100,2,2,3,3,4,5,5,6,7]))
