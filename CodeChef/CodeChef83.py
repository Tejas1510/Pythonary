""""""""""""""""""""""""""""""""""""""
Name of Question:Find Your Gift
Link of Question:https://www.codechef.com/problems/GIFTSRC
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    x=0
    y=0
    n=int(input())
    s=input()
    a=[]
    a.append(s[0])
    for i in range(1,len(s)):
        if((s[i]=="L" and (s[i-1]=="L" or s[i-1]=="R")) or
        (s[i]=="R" and (s[i-1]=="L" or s[i-1]=="R")) or
        (s[i]=="U" and (s[i-1]=="U" or s[i-1]=="D")) or
        (s[i]=="D" and (s[i-1]=="U" or s[i-1]=="D"))):
            pass
        else:
            a.append(s[i])
    for i in range(len(a)):
        if(a[i]=="L"):
            x=x-1
        elif(a[i]=="R"):
            x=x+1
        elif(a[i]=="U"):
            y=y+1
        elif(a[i]=="D"):
            y=y-1
    print(x,y)
