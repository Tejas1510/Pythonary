a=["H","Q","9"]
s=input()
flag=0
for i in range(len(s)):
    if(s[i] in a):
        flag=1
        break
if(flag==0):
    print("NO")
else:
    print("YES")
