#hacker rank 10 days of statistics
#https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
#day 0: weighted mean


def weighted_mean(nums,weights):
    
    nums = [10,40,30,50,20]
    weights = [1,2,3,4,5]
    
    top = sum([nums[i] * weights[i] for i in range(len(nums))])
    bottom = sum(weights)
    
    return top / bottom


