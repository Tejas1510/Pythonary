""""""""""""""""""""""""""""""""""""""
Name of Question:Bear and Big Brother
Link of Question:https://codeforces.com/problemset/problem/791/A
"""""""""""""""""""""""""""""""""""""""
a,b=map(int,input().split())
count=0
while(a<=b):
    a=a*3
    b=b*2
    count=count+1
print(count)
