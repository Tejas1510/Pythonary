""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and the Wildcard Matching
Link of Question:https://www.codechef.com/problems/TWOSTR
"""""""""""""""""""""""""""""""""""""""

t=int(input())
for i in range(t):
    x=input()
    y=input()
    flag=0
    for i in range(len(x)):
        if(x[i]!="?" and y[i]!="?"):
            if(x[i]!=y[i]):
                flag=1
                break
    if(flag==1):
        print("No")
    else:
        print("Yes")
