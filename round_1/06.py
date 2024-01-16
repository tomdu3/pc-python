# Temperature Converter: Create a function that converts a temperature from Fahrenheit to Celsius and vice versa, based on a second argument indicating the direction of conversion ('F_to_C' or 'C_to_F').

def convert_temperature(temp, direction):
	if direction not in ['F_to_C', 'C_to_F']: return f'"{direction}" is not the right argument'
	return  (temp-32) * 5/9 if direction == 'F_to_C' else temp* 9/5 + 32

print(convert_temperature(20, 'F_to_C'))  # -6.77
print(convert_temperature(20, 'C_to_F'))  # 68.0
print(convert_temperature(20, '_to_C'))  # error

