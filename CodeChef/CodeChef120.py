""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Chef Diet
Link of Question:https://www.codechef.com/problems/DIET
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    sum=0
    flag=0
    for i in range(len(a)):
        sum=sum+a[i]
        if(sum>=k):
            sum=sum-k
        else:
            flag=1
            ans=i+1
            break
    if(flag==0):
        print("YES")
    else:
        print("NO",ans)
