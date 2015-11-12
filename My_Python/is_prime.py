# coding:utf-8
# 判断是否是素数
def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
       if n % i == 0:
           return False
       i += 1
    return True

print isPrime(27)

# 打印出素数列表
print ([x for x in range(100) if isPrime(x)])