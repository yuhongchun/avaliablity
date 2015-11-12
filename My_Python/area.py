import math 
def area(radius):
	""" Returns the area of a circle with the given radius.
	For example:
	>>>area(5.5)
	95.0331777
	"""
	return math.pi * radius ** 2 

print(area.__doc__)
print(area(5.5))
print(area(7.7))