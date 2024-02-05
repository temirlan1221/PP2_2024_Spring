def result(mylist):
	for i in range(len(mylist) - 1):
		if mylist[i] == 0 and mylist[i + 1] == 0 and mylist[i + 2] == 7:
			return True
	return False

mylist = []
n = int(input(":"))
for i in range(n):
	num = int(input(":"))
	mylist.append(num)

solution = result(mylist)
if solution:
	print("YES")
else:
	print("NO")