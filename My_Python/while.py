n = int(input('Enter an integer >=0:'))
fact = 1
i = 2 
while i <= n:
	fact = fact * i 
	i = i + 1 
print(str(n)+ ' fact is ' +str(fact))
