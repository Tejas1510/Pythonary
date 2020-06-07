""""""""""""""""""""""""""""""""""""""
Name of Question:Similar Dishes
Link of Question:https://www.codechef.com/problems/SIMDISH
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s1=list(map(str,input().split(" ")))
    s2=list(map(str,input().split(" ")))
    count=0
    for i in range(len(s1)):
        if(s1[i] in s2):
            count=count+1
    if(count>=2):
        print("similar")
    else:
        print("dissimilar")
