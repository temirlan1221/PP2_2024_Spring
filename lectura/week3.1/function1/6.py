def reverse(sentence):
	words = sentence.split()
	reversedword = ' '.join(reversed(words))
	return reversedword

sentence = input(":")

result = reverse(sentence)
print(result)