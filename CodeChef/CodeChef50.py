""""""""""""""""""""""""""""""""""""""
Name of Question:Playing with Matches
Link of Question:https://www.codechef.com/problems/MATCHES
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    sum=0
    a,b=map(int,input().split())
    dict={0:"6",1:"2",2:"5",3:"5",4:"4",5:"5",6:"6",7:"3",8:"7",9:"6"}
    c=a+b
    arr=[i for i in str(c)]
    for i in range(len(arr)):
        sum=sum+int(dict[int(arr[i])])
    print(sum)
