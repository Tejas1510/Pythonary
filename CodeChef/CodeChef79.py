""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Friends
Link of Question:https://www.codechef.com/problems/FRK
"""""""""""""""""""""""""""""""""""""""
n=int(input())
s="chef"
res =[s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)]
final=[]
for i in range(len(res)):
    if(len(res[i])!=1):
        final.append(res[i])
count=0
for i in range(n):

    s=input()
    for i in range(len(final)):
        if(s.find(final[i])==-1):
            pass
        else:
            count=count+1
            break
print(count)
