""""""""""""""""""""""""""""""""""""""
Name of Question:Simple Statistics
Link of Question:https://www.codechef.com/problems/SIMPSTAT
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(k):

        max1=a[-1]
        min1=a[0]
        a.remove(max1)
        a.remove(min1)

    print(float(sum(a)/len(a)))
