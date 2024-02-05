def solve(numheads , numlegs):
	num_chickens = 0
	num_rabbits = 0
	for num_rabbits in range(numheads + 1):
		num_chickens = numheads - num_rabbits
		if (2 * num_chickens + 4 * num_rabbits == numlegs):
			return num_chickens , num_rabbits
	return None
	

numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)
if solution :
	num_chickens , num_rabbits = solution
	print(f"The number of chicken is {num_chickens} and the number of rabbits is {num_rabbits}")
else:
	print("we dont have a answer")
