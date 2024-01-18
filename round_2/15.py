# Regular Expression Matcher: Write a function that uses regular expressions to check if a given string matches a given pattern.

import re

def check_regex(string, pattern):
    regex_pattern = re.compile(pattern)

    if regex_pattern.fullmatch(string):
        return True
    else:
        return False

print(check_regex('hello', r'\w.'))
print(check_regex('he', r'\w.'))

