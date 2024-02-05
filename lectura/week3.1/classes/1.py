class result:
	def __init__(self):
		self.text = ""
	def getString(self):
		self.text = str(input(":"))
	def printString(self):
		p = self.text.upper()
		print(p)
x = result()
x.getString()
x.printString()
