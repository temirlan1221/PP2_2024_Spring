def result(firstList):
	newList = []
	for i in firstList:
		if i not in newList:
			newList.append(i)
	return newList
	
firstList = []
n = int(input(":"))
for i in range(n):
	element = input(":")
	firstList.append(element)

answer = result(firstList)
print(answer)