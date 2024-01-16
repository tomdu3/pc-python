# Fibonacci Sequence Generator: Write a function that returns the Fibonacci sequence up to a given number of elements.

def fibonacci(n):
	fib_sequence = [0, 1]
	for i in range(2, n):
		fib_sequence.append(fib_sequence[i-2] + fib_sequence[i-1])
	return fib_sequence

print(fibonacci(15))