""""""""""""""""""""""""""""""""""""""
Name of Question:Snakes, Mongooses and the Ultimate Election
Link of Question:https://www.codechef.com/problems/SNELECT
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    sc=s.count("s")
    mc=s.count("m")
    i=0
    while(i<len(s)-1):
        if(s[i]=="s" and s[i+1]=="m" or s[i]=="m" and s[i+1]=="s"):
            sc=sc-1
            i=i+2
        else:
            i=i+1
    if(sc>mc):
        print("snakes")
    elif(sc<mc):
        print("mongooses")
    else:
        print("tie")
