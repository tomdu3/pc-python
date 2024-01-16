# Basic Calculator: Write a function that takes two numbers and a mathematical operation (add, subtract, multiply, divide) as parameters and returns the result of that operation.

def calculator(num1, num2, operation):
	if operation == 'add': return num1 + num2
	elif operation == 'subtract': return num1 - num2
	elif operation == 'multiply': return num1 * num2
	elif operation == 'divide':
		if num2 == 0:
			return 'Division by Zero Error!'
		return num1 / num2

print(calculator(1, 2, 'add'))
print(calculator(1, 2, 'subtract'))
print(calculator(1, 2, 'multiply'))
print(calculator(1, 2, 'divide'))
print(calculator(1, 0, 'divide'))

