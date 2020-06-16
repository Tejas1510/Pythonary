""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and String
Link of Question:https://www.codechef.com/JUNE20B/problems/XYSTR
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()

    if(len(set(s))==1):
        print(0)
    else:
        i=0
        count=0
        while(i<len(s)-1):
            if((s[i]=="x" and s[i+1]=="y") or (s[i]=="y" and s[i+1]=="x")):
                count=count+1
                i=i+2
            else:
                i=i+1
                pass

        print(count)
