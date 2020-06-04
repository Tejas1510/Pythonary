""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Rainbow Array
Link of Question:https://www.codechef.com/problems/RAINBOWA
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a1=a[::-1]
    if(set(a)=={1,2,3,4,5,6,7} and a1==a):
        print("yes")
    else:
        print("no")
