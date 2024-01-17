# Palindromic Substrings: Write a function that finds and returns all
# the palindromic substrings of a given string.

def find_palindromes(string):
    palindromes = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1]:
                palindromes.append(substring)
    return sorted(set(palindromes))


# Test cases
print(find_palindromes("aba"))
print(find_palindromes("abba"))
print(find_palindromes("abc"))
print(find_palindromes("bababab"))
