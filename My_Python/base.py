#encoding:utf-8
#此实例用于演示常见内置属性的用法。
class Fruit:
	def __init__(self):
		self.__color = "red"

class Apple(Fruit):
	'''
	This is a test doc.
	'''

if __name__ == "__main__":
	fruit = Fruit()
	apple = Apple()
	print Apple.__bases__ #用于输出基类组成的元组
	print apple.__doc__
	print apple.__module__
	print apple.__dict__ #此行代码输出apple对象中属性组成的字典。