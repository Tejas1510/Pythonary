# How to find target Sum with the help of two number of an array in o(n) time
#It can be easily found using brute force in o(n^2) but in Compitive programming this
# approach will give TLE
#So this Solution
# Here a is the array and Target Sum is the required Sum

def Solution(a,TargetSum):
    nums={}
    for i in range(len(a)):
        if(TargetSum-a[i] in nums):
            return [a[i],TargetSum-a[i]]
        else:
            nums[a[i]]=True
    return -1

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    TargetSum=int(input())
    a=Solution(a,TargetSum)
    print(*a)
