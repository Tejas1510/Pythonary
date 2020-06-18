""""""""""""""""""""""""""""""""""""""
Name of Question:Bear and Segment 01 
Link of Question:https://www.codechef.com/problems/SEGM01
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input().rstrip("0")
    a=list(s)

    b=sorted(a)
    if(len(a)==0):
        print("NO")
    elif(b==a and len(a)!=0):
        print("YES")
    else:
        print("NO")
