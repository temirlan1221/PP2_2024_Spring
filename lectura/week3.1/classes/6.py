def prime():
	num = int(input(":"))
	size = (num // 2) + 1
	for i in range(2,size,1):
		if num % i == 0: 
			return False
	return True
solution = prime()
if solution:
	print("This is a prime number")
else:
	print("This is not a prime number")