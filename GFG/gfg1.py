""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Arya and The Great War
Link of Question:https://practice.geeksforgeeks.org/problems/arya-and-the-great-war/0
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
        count=0
        n=int(input())
        c=bin(n)
        c=c.replace("0b","")
        d=list(map(int,str(c)))
        for i in range(0,len(d)):
            if(d[i]==1):
                count=count+1
        print(count)
