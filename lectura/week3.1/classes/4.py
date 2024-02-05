class Point:
	def __init__(self , x , y):
		self.x = x
		self.y = y
	def show(self):
		print("first coordinate:{}".format(self.x))
		print("second coordinate:{}".format(self.y))
	def move(self):
		print("We change these two coordinates {},{}".format(self.x,self.y))
		first = int(input(":"))
		second = int(input(":"))
		self.x = first
		self.y = second
	def dist(self):
		sumOfCoordinates = abs(self.x - self.y)
		print(sumOfCoordinates)
xy = Point(5,3)
xy.show()
xy.move()
xy.dist()