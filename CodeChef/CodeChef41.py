""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Cook Off
Link of Question:https://www.codechef.com/problems/CCOOK
"""""""""""""""""""""""""""""""""""""""
n=int(input())
for i in range(n):
    count=0
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if(a[i]==1):
            count=count+1
    if(count==0):
        print("Beginner")
    elif(count==1):
        print("Junior Developer")
    elif(count==2):
        print("Middle Developer")
    elif(count==3):
        print("Senior Developer")
    elif(count==4):
        print("Hacker")
    elif(count==5):
        print("Jeff Dean")
