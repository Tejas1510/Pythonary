""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Gems Stone
Link of Question:https://www.hackerrank.com/challenges/gem-stones/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
res=""
ans=0
for i in range(t):
    s=input()
    s=list(set(s))
    s="".join(s)
    res=res+s
final=list(set(res))

for i in range(len(final)):
    if(res.count(final[i])==t):
        ans=ans+1
    else:
        pass
print(ans)
