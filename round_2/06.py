# Leap Year Verifier: Create a function that checks if
# a given year is a leap year.

def leap_year_verify(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap_year_verify(2000))
print(leap_year_verify(2023))
print(leap_year_verify(1900))
