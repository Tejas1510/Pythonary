""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Encryption
Link of Question:https://www.hackerrank.com/challenges/encryption/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import math as m
def function(str, k):

    for i in range(len(str)):
        if i%k == 0:
            sub = str[i:i+k]
            lst = []
            for j in sub:
                lst.append(j)


    for i in range(0,k):

        a=str[i::k]
        print(''.join(a),end=" ")
s=input()
s=s.replace(" ","")
len1=len(s)
row=m.floor(m.sqrt(len1))
coulomn=m.ceil(m.sqrt(len1))
function(s,coulomn)
