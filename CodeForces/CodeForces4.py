""""""""""""""""""""""""""""""""""""""
Name of Question:Team
Link of Question:http://codeforces.com/problemset/problem/231/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
count=0
for i in range(n):
    a=list(map(int,input().split()))
    if(a.count(1)>=2):
        count=count+1
print(count)
