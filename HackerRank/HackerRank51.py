from collections import OrderedDict
s=input()
a=list(OrderedDict.fromkeys(s))

b=[]
for i in range(len(a)):
    if(s.count(a[i])%2!=0):
        b.append(a[i])
if(len(b)==0):


    print("Empty String")
else:
    s="".join(b)

    print(s)
