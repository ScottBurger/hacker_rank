#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics



def mdn(x):
    if len(x) % 2 == 0:
      return sum(sorted(x)[len(x)//2-1:len(x)//2+1])//2.0 
    else:
      return sorted(x)[len(x)//2]
        
    
def quarts(x = [1,2,3,4]):
        
    lower = [i for i in x if i<mdn(x)]
    upper = [i for i in x if i>mdn(x)]
    
    q1 = mdn(lower)
    q2 = mdn(x)
    q3 = mdn(upper)
    
    return [q1, q2, q3]
    

quarts([3,7,8,5,12,14,21,13,18])


