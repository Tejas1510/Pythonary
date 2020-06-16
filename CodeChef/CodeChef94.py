""""""""""""""""""""""""""""""""""""""
Name of Question:Who dares to be a millionaire
Link of Question:https://www.codechef.com/problems/WDTBAM
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    s1=input()
    s2=input()
    count=0
    a=list(map(int,input().split()))
    for i in range(0,len(s1)):
        if(s1[i]==s2[i]):
            count=count+1
    if(count==n):
        print(a[n])
    elif(count==0):
        print(a[0])
    else:
        max=0
        for i in range(0,count+1):
            if(a[i]>max):
                max=a[i]

        print(max)
