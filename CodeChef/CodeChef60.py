""""""""""""""""""""""""""""""""""""""
Name of Question:Chef Judges a Competition
Link of Question:https://www.codechef.com/problems/CO92JUDG
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    max1=max(a)
    max2=max(b)
    a.remove(max1)
    b.remove(max2)
    sum1=sum(a)
    sum2=sum(b)
    if(sum1<sum2):
        print("Alice")
    elif(sum1>sum2):
        print("Bob")
    else:
        print("Draw")
