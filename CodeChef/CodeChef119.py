""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Cook-Off Contests
Link of Question:https://www.codechef.com/problems/C00K0FF
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        s=input()
        a.append(s)
    a=list(set(a))
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    if("cakewalk" in a):
        count1=1
    if("simple" in a):
        count2=1
    if("easy" in a):
        count3=1
    if("easy-medium" in a or "medium" in a):
        count4=1
    if("medium-hard" in a or "hard" in a):
        count5=1

    if(count1==1 and count2==1 and count3==1 and count4==1 and count5==1):
        print("Yes")
    else:
        print("No")
