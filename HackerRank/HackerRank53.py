""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Alternating Characters
Link of Question:https://www.hackerrank.com/challenges/alternating-characters/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    count=0
    s=input()
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count=count+1
        else:
            pass
    print(count)
