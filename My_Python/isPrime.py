def isPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


print isPrime(50)
print ([x for x in range(2,51) if isPrime(x)])

