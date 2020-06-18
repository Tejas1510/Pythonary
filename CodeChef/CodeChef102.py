""""""""""""""""""""""""""""""""""""""
Name of Question:Xenny and Alternating Tasks
Link of Question:https://www.codechef.com/problems/XENTASK
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sum1=[]
    sum2=[]
    sum3=[]
    sum4=[]
    for i in range(0,len(a),2):
        sum1.append(a[i])
    for i in range(1,len(a),2):
        sum2.append(a[i])
    for i in range(0,len(b),2):
        sum3.append(b[i])
    for i in range(1,len(b),2):
        sum4.append(b[i])
    print(min(sum(sum1)+sum(sum4),sum(sum2)+sum(sum3)))
