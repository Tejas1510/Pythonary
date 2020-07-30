""""""""""""""""""""""""""""""""""""""
Name of Question:Chef in Fantasy League
Link of Question:https://www.codechef.com/problems/FFL
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    arr1=[]
    arr2=[]
    arr3=[]
    arr4=[]
    if(len(set(b))==1):
        print("no")
    else:
        for i in range(len(b)):
            if(b[i]==0):
                arr1.append(i)
            elif(b[i]==1):
                arr2.append(i)
        for i in range(len(arr1)):
            arr3.append(a[arr1[i]])

        for i in range(len(arr2)):
            arr4.append(a[arr2[i]])

        if(min(arr3)+min(arr4)+s<=100):
            print("yes")
        else:
            print("no")
