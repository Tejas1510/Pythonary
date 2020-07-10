#Modification of last Day Question
#Find a triplet that sum to a given value
#Brute Force approach requires o(n^3)
#We will Solve it with the help of hash map in O(n^2) approach
#This question has been asked in multiple times in most of the FANNG Company interview

def Solution(a,TargetSum):
    for i in range(0,len(a)-1):
        nums={}
        current_sum=TargetSum-a[i]
        for j in range(1,len(a)):
            if(current_sum-a[j] in nums):
                return [a[j],a[i],current_sum-a[j]]
            else:
                nums[a[j]]=True
    return -1

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    TargetSum=int(input())
    a=Solution(a,TargetSum)
    print(*a)
