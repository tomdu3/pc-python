# Word Occurrence in Sentence: Create a function that counts how many times a word occurs in a sentence (passed as a string).

def word_occurence(sentence, word):
	return sentence.lower().split().count(word.lower())

with open('kafka-trial.txt', 'r') as f:
	sentence = f.read().replace('\n', ' ')

print(word_occurence(sentence, 'judge'))