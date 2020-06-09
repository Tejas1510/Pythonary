""""""""""""""""""""""""""""""""""""""
Name of Question:Bit++
Link of Question:https://codeforces.com/problemset/problem/282/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
n=int(input())
count=0
for i in range(n):
    s=input()
    if(s=="X++"):
        count=count+1
    elif(s=="++X"):
        count=count+1
    elif(s=="--X"):
        count=count-1
    elif(s=="X--"):
        count=count-1
print(count)
