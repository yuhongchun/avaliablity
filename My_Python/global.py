name = 'Jack'
def say_hello():
	print('Hello,' + name + '!')
def change_name(new_name):
	global name 
	name = new_name

print(say_hello())

change_name('pip')
print(say_hello())