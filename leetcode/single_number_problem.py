### problem name single number on leetcode

def example(nums):
    l= []
    for i in nums:
        if i in l:
            l.remove(i)
        else:
            l.append(i)    
    return l

if __name__ == "__main__":
    nums= [1,2,2,3,3,4]
    a= example(nums) 
    print(*a)  
# 

