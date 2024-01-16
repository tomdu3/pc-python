# Function to Summarize a Text File: Write a function that accepts a filename as a parameter, reads the file, and returns the number of lines, words, and characters in the file.

def  summarize_text_file(filename):
	with open(filename, 'r') as file:
		content = file.read()
	lines = content.split('\n')
	words = [word for line in lines for word in line.split()]
	characters = [character for character in content]

	print(len(lines), len(words), len(characters))

summarize_text_file('kafka-trial.txt')