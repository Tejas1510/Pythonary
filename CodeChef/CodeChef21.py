""""""""""""""""""""""""""""""""""""""
Name of Question:Two vs Ten
Link of Question:https://www.codechef.com/problems/TWOVSTEN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    x=int(input())
    if((x%10==0 and x>9) or x==0):
        print(0)
    elif(x%5==0 and x>4):
        print(1)
    else:
        print(-1)
