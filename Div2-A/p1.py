s=input()
s=s.lower()
a=["a",'e',"i","o","u","y"]
s1=""
for i in range(len(s)):
    if(s[i] in a):
        pass
    else:
        s1=s1+"."+s[i]
print(s1)
