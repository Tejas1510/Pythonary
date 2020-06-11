""""""""""""""""""""""""""""""""""""""
Name of Question:Snake Procession
Link of Question:https://www.codechef.com/problems/SNAKPROC
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    s=s.replace(".","")
    if(len(s)==0):
        print("Valid")
    else:
        a=s.count("HT")
        if(a==len(s)/2):
            print("Valid")
        else:
            print("Invalid")
