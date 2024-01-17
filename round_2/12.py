# Circular Prime Checker: Develop a function that checks if all rotations of a number's digits are prime.

def check_prime(n):	
    for i in range(2, int(n/(n**0.5)+1)):
        if not (n % i):
            return False
    return True

def prime_checker(num):
    num_string = str(num)
    for i in range(len(num_string)):
        n = int(num_string[i:] + num_string[:i])
        if not check_prime(n):
            return False
    return True

print(prime_checker(919))
print(prime_checker(217))

