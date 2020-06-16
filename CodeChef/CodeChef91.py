""""""""""""""""""""""""""""""""""""""
Name of Question:Bear and Milky Cookies
Link of Question:https://www.codechef.com/problems/COOMILK
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a=s.split(" ")
    flag=0
    if(len(set(a))==1 and "cookie" in a):
        print("NO")
    else:
        for i in range(len(a)):
            if(a[i]=="cookie" and i==len(a)-1):
                flag=1
                break
            if(a[i]=="cookie" and a[i+1]!="milk"):
                flag=1

        if(flag==1):
            print("NO")
        else:
            print("YES")
