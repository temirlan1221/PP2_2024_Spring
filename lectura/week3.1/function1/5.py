from itertools import permutations
def print_permutation():
	text = input(":")
	result = list(permutations(text))

	print("Permutations of '{}'".format(text))
	for per in result:
		print(per)

print_permutation()
