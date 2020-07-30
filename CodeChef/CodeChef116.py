""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Multiple Choice Exam
Link of Question:https://www.codechef.com/problems/EXAM1
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    corans=input()
    chefans=input()
    count=0
    i=0
    while(i<n):
        if(corans[i]==chefans[i]):
            count=count+1
            i=i+1
        elif(corans[i]!=chefans[i] and chefans[i]=="N"):
            i=i+1
        elif(corans[i]!=chefans[i]):
            i=i+2
    print(count)
