# Email Validator: Write a function that checks if a given string is a valid email address (contains one '@' and at least one '.').

def check_valid_email(email):
	return '@' in email and '.' in email

print(check_valid_email('tomdu3@ymail.com'))