#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
#day 0: mean, median, mode

def mdn(x):
    if len(x) % 2 == 0:
      return sum(sorted(x)[len(x)//2-1:len(x)//2+1])/2.0 
    else:
      return sorted(x)[len(x)//2]
  
    
def mean(x):
    return sum(x) / len(x)



def mode(x):
    b = {}
    for item in x:
        b[item] = b.get(item, 0) + 1
        
    if max(b.values()) == min(b.values()):
        b_sorted = sorted(b.keys())
        return b_sorted[0]
    else:
        b_sorted = sorted(b, key=b.get, reverse=True)
        return b_sorted[0]
     


        
x = [1,1,3,4,5,9,9,9,10]
mode(x)

y = [5,4,3,2,1]
mode(y)

z = [64630,11735,14216,99233,14470,4978,73429,38120,51135,67060]
mode(z)
mdn(z)
mean(z)
