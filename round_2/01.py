# CSV Column Averager: Write a function that reads a CSV file and calculates the average of the numbers in a given column.
# Hint: Use the csv module to read the file and remember to skip the header row. Convert the column values to floats before averaging.

import csv

def table_column_avg(table,headers,column):
	column_index = headers.index(column)
	if isinstance(table[0][column_index], str):
		return f'Error: Column "{column}" has non numeric values'
	column_average = sum([row[column_index]. for row in table])/len(table)
	return column_average


table = []

with open('test.csv', 'r') as f:
	csv_content = csv.reader(f)


	headers = next(csv_content)

	for row in csv_content:
		row_list = [float(item) if item.isnumeric() else item for item in row]

		table.append(row_list)

print(headers)
print(table_column_avg(table,headers,'age'))
print(table_column_avg(table,headers,'years_of_employment'))
print(table_column_avg(table,headers,'firstname'))



