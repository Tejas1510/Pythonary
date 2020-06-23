""""""""""""""""""""""""""""""""""""""
Name of Question:A - Books
Link of Question:https://www.codechef.com/problems/BIT2A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    count=0
    if(len(set(a))==0):
        for i in range(len(a)):
            print(0,end=" ")
    else:
        for i in range(len(a)):
            for j in range(1,len(a)):
                if(a[i]<a[j]):
                    count=count+1
            b.append(count)
            count=0
        print(*b)
