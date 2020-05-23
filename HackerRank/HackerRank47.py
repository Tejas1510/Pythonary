""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Service Lane
Link of Question:https://www.hackerrank.com/challenges/service-lane/problem?h_r=next-challenge&h_v=zen
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
n,t=map(int,input().split())
a=list(map(int,input().split()))
while(t!=0):
    i,j=map(int,input().split())
    t=t-1
    b=a[i:j+1]
    print(min(b))
