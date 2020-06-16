""""""""""""""""""""""""""""""""""""""
Name of Question:Bear and Ladder
Link of Question:https://www.codechef.com/problems/BRLADDER
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(abs(a-b)==2):
        print("YES")
    elif((a-b)==1 and a%2==0):
        print("YES")
    elif((a-b)==1 and a%2==0):
        print("YES")
    elif((b-a)==1 and b%2==0):
        print("YES")
    else:
        print("NO")
