""""""""""""""""""""""""""""""""""""""
Name of Question:Good and Bad Person
Link of Question:https://www.codechef.com/problems/GOODBAD
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    brother=0
    chef=0
    for i in range(len(s)):
        if(s[i].isupper()):
            brother=brother+1
        else:
            chef=chef+1
    min1=min(brother,chef)
    max1=max(brother,chef)
    if(min1>k):
        print("none")
    elif(max1<=k):
        print("both")
    elif(chef>brother):
        print("chef")
    else:
        print("brother")
