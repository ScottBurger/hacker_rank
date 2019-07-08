#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

import random

def dice(n):
    total = 0
    for i in range(n):
        total += random.randint(1, 6)
    return total

results = []
for i in range(1,100):
    results.append(dice(2))

sum(1 for x in results if x <= 9) / len(results)

#the wording here can be confusing, but the key point is that the sum can't be more than 9
#from the answers available, 5/6 is closest to our result of 0.8