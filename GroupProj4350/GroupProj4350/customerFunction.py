from placeOrder import *
from history import *

class Customer:
	
	def __init__(self,server, uname, pword):
		self.id=''
		self.name =''
		self.phone=''
		self.preference=''
		self.username=uname
		self.password=pword
		self.CustomerLogin(server)

	def CustomerLogin(self, server):
		cust = server.sqlSelect("SELECT * FROM customers WHERE customer_username= '%s'"% self.username)
		cust = cust.fetchone()
		if cust is None:
			print("Invalid Username")
		elif cust[5] != self.password:
			print("Password and UserName Does Not Match!")
		else:
			print("Welcome " + cust[1] + "!")
			self.id = str(cust[0])
			self.name =str(cust[1])
			self.preference=str(cust[3])
			self.phone=str(cust[2])
			self.signedIn(server)
		
	def signedIn(self, server):
		while 1:
			print("---Customer Menu---")
			print("1. Place an Order")
			print("2. History")
			print("3. Sign Out")
			userInput = int(input())
			if userInput == 1:
				PlaceOrder()
			elif userInput == 2:
				History(self, server)
			elif userInput ==3:
				break
			else:
				print("Not an option!")