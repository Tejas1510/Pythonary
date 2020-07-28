n=int(input())
s=input()
a=list(s)
s1=""
b=[]
for i in range(len(a)):
    if(a[i]=="x"):
        s1=s1+"x"
    else:
        b.append(s1)
        s1=""
b.append(s1)
sum=0
for i in range(len(b)):
    if(len(b[i])>2):
        sum=sum+len(b[i])-2
print(sum)
