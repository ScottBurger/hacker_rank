#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics



def mdn(x):
    if len(x) % 2 == 0:
      return sum(sorted(x)[len(x)//2-1:len(x)//2+1])//2.0 
    else:
      return sorted(x)[len(x)//2]
        
    
def iqr(x):
    
    lower = [i for i in x if i<mdn(x)]
    upper = [i for i in x if i>mdn(x)]
    
    q1 = mdn(lower)
    q3 = mdn(upper)
        
    return q3 - q1



iqr([6, 6, 6, 6, 6, 8, 8, 8, 10, 10, 12, 12, 12, 12, 16, 16, 16, 16, 16, 20])

