#encoding:utf-8
#类方法使用举例说明，分别用到了@staticmethod和staticmethod()
'''我们这里定义的__color是私有属性，__get_Price()是私有方法。如果直接访问的话，会提示找不到相关的属性或者方法，
但是如果你真要访问私有的相关数据的话， 也是可以访问的，严格地说，私有方法在它们的类外是可以访问的，只是不容易
处理。在Python中没有什么是真正私有的。在内部，私有方法和属性的名字被忽然改变和恢复，以致于使得它们看上去用
它们给定的名字是无法使用的。
'''
class Fruit:
	price = 0     #类变量

	def __init__(self):
		self.__color = "red"  #定义私有属性

	def getColor(self):
		print self.__color

	@staticmethod
	def getPrice():
		print Fruit.price

	def __getPrice(): #定义私有方法
		Fruit.price = Fruit.price + 10
		print Fruit.price

	count = staticmethod(__getPrice)

if __name__ == "__main__":
	apple = Fruit() #实例化apple
	apple.getColor() #使用实例调用静态方法
	Fruit.count() #使用类名调用静态方法
	banana = Fruit()
	Fruit.count()
	Fruit.getPrice()
