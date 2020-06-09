""""""""""""""""""""""""""""""""""""""
Name of Question:Tram
Link of Question:https://codeforces.com/problemset/problem/116/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
sum=0
arr=[]
for i in range(t):
    a,b=map(int,input().split())
    arr.append(sum)
    sum=sum-a+b
print(max(arr))
