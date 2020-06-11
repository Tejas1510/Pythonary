""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and String
Link of Question:https://www.codechef.com/problems/CHRL2
"""""""""""""""""""""""""""""""""""""""
s=input()
c=0
ch=0
che=0
chef=0
for i in s:
    if i=='C':
        c+=1
    elif i=='H' and c>ch:
        ch+=1
    elif i=='E' and ch>che:
        che+=1
    elif i=='F' and che>chef:
        chef+=1
print(chef)
