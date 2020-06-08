""""""""""""""""""""""""""""""""""""""
Name of Question:Ada School
Link of Question:https://www.codechef.com/problems/ADASCOOL
"""""""""""""""""""""""""""""""""""""""
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    if (n*m)%2==0:
        print("YES")
    else:
        print("NO")
