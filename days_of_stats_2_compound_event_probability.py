#hacke'r' 'r'ank 10 days of statistics
#https://www.hacke'r''r'ank.com/domains/tuto'r'ials/10-days-of-statistics

import random

urn_1 = ['r','r','r','r','b','b','b']
urn_2 = ['r','r','r','r','r','b','b','b','b']
urn_3 = ['r','r','r','r','b','b','b','b']


results = []
for i in range(0,10000):
    picks = [random.choice(urn_1), random.choice(urn_2), random.choice(urn_3)]
    results.append(picks)

sum(1 for x in range(len(results)) if (results[x].count('r') == 2 and results[x].count('b') == 1)) / len(results)
