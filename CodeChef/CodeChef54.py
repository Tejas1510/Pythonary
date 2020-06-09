""""""""""""""""""""""""""""""""""""""
Name of Question:From heaven to Earth
Link of Question:https://www.codechef.com/problems/ELEVSTRS
"""""""""""""""""""""""""""""""""""""""
import math as m
t=int(input())
for i in range(t):
    n,v1,v2=map(int,input().split())
    a1=m.sqrt(2)*n/v1
    a2=2*n/v2
    if(a1<a2):
        print("Stairs")
    elif(a1>a2):
        print("Elevator")
    else:
        print("Stairs")
