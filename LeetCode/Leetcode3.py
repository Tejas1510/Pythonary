""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Jewels and Stones
Link of Question:https://leetcode.com/problems/jewels-and-stones/
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
j=input()
s=input()
n=list(j)
count=0
from collections import Counter
c=Counter(list(s))
for i in range(0,len(j)):
    if(j[i] in c):
        count=count+c.get(j[i])
print(count)
