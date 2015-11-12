class Animal(object):
    def run(self):
        print 'Animal is running...'
    def run_twice(self):
        self.run()
        self.run()

class Dog(Animal):
    def run(self):
    	print "Dog is running..."
    def eat(self):
    	print "Eating meat..."

class Cat(Animal):
    def run(self):
    	print "Cat is runnig..."
class Tortoise(Animal):
	def run(self):
		print "Tortoise is runnig slowly"

dog = Dog()
dog.run()
dog.eat()
dog.run_twice()

tor = Tortoise()
tor.run_twice()



