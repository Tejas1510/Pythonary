""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and his Student
Link of Question:https://www.codechef.com/problems/CHEFSTUD
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    a=list(s)
    for i in range(len(a)):
        if(a[i]=="<"):
            a[i]=">"
        elif(a[i]==">"):
            a[i]="<"
    s="".join(a)

    print(s.count("><"))
