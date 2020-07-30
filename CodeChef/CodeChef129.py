t=int(input())
for i in range(t):
    s1=""
    s2=""
    for i in range(3):
        s=input()
        s1=s1+s
    print(s1)
    for i in range(len(s1)):
        if(s1[i]=="l"):
            s2=s2+str(i)
    print(s2)
    if("034" in s2):
        print("yes")
    elif("145" in s2):
        print("yes")
    elif("13678" in s2):
        print("yes")
    else:
        print("no")
