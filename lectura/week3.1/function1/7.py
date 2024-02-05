def result(mylist):
	for i in range(len(mylist) - 1):
		if mylist[i] == 3 and mylist[i + 1]:
			return True
		
	return False

mylist = []
n = int(input(":"))
for i in range(n):
	element = int(input(":"))
	mylist.append(element)
solution = result(mylist)
if solution:
	print("True")
else:
	print("False")