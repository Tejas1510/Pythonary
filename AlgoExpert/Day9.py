# print a fibonacii series
# Here we will use two approaches
# 1.recurrsion 2.Dynammic Programming

#using recurrsion
#Time Complexity O(2^n) and Space Complexity O(n)
def recursive(n):
    if(n==1):
        return(0)
    elif(n==2):
        return(1)
    else:
        return recursive(n-1)+recursive(n-2)
#Time Complexity O(n) and Space Complexity O(n)
def Dynammic(n):
    a=[0]*n
    a[0]=0
    a[1]=1
    for i in range(2,len(a)):
        a[i]=a[i-1]+a[i-2]
    return sum(a)

t=int(input())
for i in range(t):
    n=int(input())
    ans1=recursive(n)
    print(ans1)
    ans2=Dynammic(n)
    print(ans1)
