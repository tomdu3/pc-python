# Multiplication Table Printer: Develop a function that prints out a multiplication table for numbers up to a given number.

def print_multiplication_table(n):
	for i in range(1, n+1):
		for j in range(1, n+1):
			print(i*j, end='')
			if i*j//10 == 0:
				print('  |', end='')
			elif i*j//100 == 0:
				print(' |', end='')
			else:
				print('|', end='')
		print('')

print_multiplication_table(10)