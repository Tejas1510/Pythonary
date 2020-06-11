""""""""""""""""""""""""""""""""""""""
Name of Question:Play piano
Link of Question:https://www.codechef.com/problems/PLAYPIAN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    flag=0
    arr=[]
    if(len(s)==2):
        if(s[0]==s[1]):
            flag=1

    else:
        for i in range(0,len(s),2):
            s1=s[i:i+2]
            arr.append(s1)
        for i in range(len(arr)):
            s2=arr[i]
            if(s2[0]==s2[1]):
                flag=1
                break
            else:
                continue

    if(flag==0):
        print("yes")
    else:
        print("no")
