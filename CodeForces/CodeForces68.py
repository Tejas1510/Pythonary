dict={"purple":"Power","green":"Time","blue":"Space","orange":"Soul","red":"Reality","yellow":"Mind"}
n=int(input())
a=[]
for i in range(n):
    s=input()
    dict.pop(s)
for k,v in dict.items():
    a.append(v)
print(len(a))
for i in range(len(a)):
    print(a[i])
