import csv

def table_column_avg(table,headers,column):
	column_index = headers.index(column)
	if isinstance(table[0][column_index], str):
		return f'Error: Column "{column}" has non numeric values'
	column_average = sum([row[column_index] for row in table])/len(table)
	return column_average


table = []

with open('test.csv', 'r') as f:
	csv_content = csv.reader(f)


	headers = next(csv_content)

	for row in csv_content:
		row_list = [int(item) if item.isnumeric() else item for item in row]

		table.append(row_list)

print(headers)
print(table_column_avg(table,headers,'age'))
print(table_column_avg(table,headers,'years_of_employment'))
print(table_column_avg(table,headers,'firstname'))



