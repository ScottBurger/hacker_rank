#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics

import random

def dice(n):
    total = []
    for i in range(n):
        total.append(random.randint(1, 6))
    return total

results = []
for i in range(100000):
    results.append(dice(2))

sum(1 for x in range(len(results)) if ((results[x][0] != results[x][1]) and (results[x][0]+results[x][1] == 6))) / len(results)

