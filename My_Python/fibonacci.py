def fib(n):   
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a,end=' ')
		a, b = b, a+b
	print()

print(fib.__doc__)
fib(10)