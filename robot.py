# print(900 * 2* 1.25 * 100 * 1.06)
# robot_price = 900
# print(robot_price * 2 * 1.25 + 100 * 1.06)
# robot_count=2
# robot_tax=1.25
# book_price=100
# book_tax=1.06
# print (robot_price * robot_count * robot_tax + book_price * book_tax)
# robot={
# "robot.price": 900,
# "robot.count":2,
# "robot.tax":1.25,
# }
class Product:
	price = 0
	count = 0
	tax = 1.25
	def price_with_tax(self):
		return self.price *self.count * self.tax
robot= Product()
robot.price=900
robot.count=2
robot.tax=1.25
book= Product ()
book.price=100
book.count=1
book.tax= 1.06
print(robot.price_with_tax()+ book.price_with_tax())








