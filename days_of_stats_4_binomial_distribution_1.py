#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

from math import factorial

#b,g = [float(i) for i in input().strip().split(' ')]
b=1.09
g=1
#print(b,g)
n=6

p = b / (b+g) 
q = 1-p
#print(p,q)
b3 = factorial(n)/(factorial(3)*factorial(n-3))* p**3 * q**(n-3)
b4 = factorial(n)/(factorial(4)*factorial(n-4))* p**4 * q**(n-4)
b5 = factorial(n)/(factorial(5)*factorial(n-5))* p**5 * q**(n-5)
b6 = factorial(n)/(factorial(6)*factorial(n-6))* p**6 * q**(n-6)
print(round(b3+b4+b5+b6,3))