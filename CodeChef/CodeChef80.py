""""""""""""""""""""""""""""""""""""""
Name of Question:Attendance
Link of Question:https://www.codechef.com/problems/ATTND
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
     b=[]
     a=[]
     n=int(input())
     for i in range(n):
         s=input()
         a1=s.split(" ")
         a.append(s)
         b.append(a1[0])
     for i in range(len(a)):
        s1=a[i]
        a1=s1.split(" ")
        if(b.count(a1[0])>1):
            print(a[i])
        else:
            s1=a[i]
            a1=s1.split(" ")
            print(a1[0])
