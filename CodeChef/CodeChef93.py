""""""""""""""""""""""""""""""""""""""
Name of Question:Whats in the name
Link of Question:https://www.codechef.com/problems/NITIKA
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()

    a=s.split(" ")

    if(len(a)==1):
        print(a[0].capitalize())
    elif(len(a)==2):
        b=a[0]
        print(b[0].upper()+"."+" "+a[1].capitalize())
    elif(len(a)==3):
        b=a[0]
        c=a[1]
        print(b[0].upper()+"."+" "+c[0].upper()+"."+" "+a[2].capitalize())
