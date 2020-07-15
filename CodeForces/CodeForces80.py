s=input()
i=0
a=[]
while(i<=len(s)-1):
    if(s[i]=="."):
        a.append("0")
        i=i+1
    else:
        if(s[i]=="-" and s[i+1]=="."):
            a.append("1")
            i=i+2
        else:
            a.append("2")
            i=i+2
s=""
s="".join(a)
print(s)
