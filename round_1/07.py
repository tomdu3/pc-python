# Prime Number Finder: Write a function that takes an integer and returns a list of all prime numbers up to and including that integer.

def find_primes(n):	
	primes = []
	for i in range(2, n+1):
		is_prime = True
		for j in range(2,int(i/(i**0.5))+1):
			print(i,j)
			if i != j and i % j == 0:
				is_prime = False
		if is_prime: primes.append(i)
	return primes

print(find_primes(100))
