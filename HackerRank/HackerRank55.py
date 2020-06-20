""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:The Love-Letter Mystery
Link of Question:https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    sum=0
    for i in range(len(s)//2):
        sum=sum+abs(ord(s[i])-ord(s[len(s)-1-i]))
    print(abs(sum))
