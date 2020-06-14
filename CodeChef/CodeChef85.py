""""""""""""""""""""""""""""""""""""""
Name of Question:Three Friend
Link of Question:https://www.codechef.com/problems/THREEFR
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    arr=[a,b,c]
    max1=max(arr)
    arr.remove(max1)
    res=sum(arr)-max1
    if(res==0):
        print('yes')
    else:
        print('no')
