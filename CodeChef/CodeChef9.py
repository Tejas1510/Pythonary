""""""""""""""""""""""""""""""""""""""
Name of Question:Grade the Steel
Link of Question:https://www.codechef.com/problems/FLOW014
"""""""""""""""""""""""""""""""""""""""

a=int(input())
for i in range(0,a):
    a,b,c=map(float,input().split())
    if(a>50 and b<0.7 and c>5600):
        print("10")
    elif(a>50 and b<0.7 and c<=5600):
        print("9")
    elif(a<=50 and b<0.7 and c>5600):
        print("8")
    elif(a>50 and b>=0.7 and c>5600):
        print("7")
    elif(a>50 or b<0.7 or c>5600):
        print("6")
    else:
        print("5")
