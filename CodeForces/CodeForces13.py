""""""""""""""""""""""""""""""""""""""
Name of Question:Solider and Bananas
Link of Question:https://codeforces.com/problemset/problem/546/A
"""""""""""""""""""""""""""""""""""""""
k,n,w=map(int,input().split())
k1=1
sum=0
while(w!=0):
    sum=sum+k1*k
    w=w-1
    k1=k1+1
if(sum<n):
    print(0)
else:
    print(abs(sum-n))
