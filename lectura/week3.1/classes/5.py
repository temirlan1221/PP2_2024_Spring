class Bank:
	def __init__(self, owner , balance):
		self.owner = owner
		self.balance = balance
	
	def withdraw(self):
		if balance <= 0:
			print("You can not withdraw money because you dont have money")
		elif balance > 0:
			sum = int(input("What sum do you want to withdraw:"))
			if sum < balance:
				self.balance -=sum
				print("You withdraw {} and you have {}".format(sum,self.balance))
	def deposit(self):
		sum = int(input("Which sum do you want to add:"))
		self.balance += sum
		print("Your balance is {}".format(self.balance))

owner = str(input("What is your name: "))
balance = int(input("Enter your initial balance: "))

operation = input("Hello Mukhameali.What do you want to do? (deposit/withdraw): ")
account = Bank(owner,balance)
if operation == "deposit":
	account.deposit()
elif operation == "withdraw":
	account.withdraw()
else:
	print("operation invalid")
		