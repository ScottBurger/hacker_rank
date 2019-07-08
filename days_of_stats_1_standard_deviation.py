#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics



def std_dev(x):
    
    mean = sum(x) / len(x)

    sq_dist = []
    for i in range(len(x)):
        sq_dist.append((x[i] - mean)**2)
        
    return (sum(sq_dist)/len(x))**(1/2)
        
    
test = [10,40,30,50,20]
std_dev(test)
