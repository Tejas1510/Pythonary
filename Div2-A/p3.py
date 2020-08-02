s=input()
h=s.count("h")
e=s.count("e")
l=s.count("l")
o=s.count("o")
flag=0
if(h<1 or e<1 or l<2 or o<1 ):
    print("NO")
else:
    h1=s.index("h")
    for i in range(h1,len(s)):
        if(s[i]=="e"):
            e1=i
            break
    else:
        flag=1
    if(flag==1):
        print("NO")
    else:
        for i in range(e1,len(s)):
            if(s[i]=="l"):
                l1=i
                break
        else:
            flag=1
        if(flag==1):
            print("NO")
        else:
            for i in range(l1+1,len(s)):
                if(s[i]=="l"):
                    l2=i
                    break
            else:
                flag=1
            if(flag==1):
                print("NO")
            else:
                for i in range(l2,len(s)):
                    if(s[i]=="0"):
                        o1=i
                        break
                else:
                    flag=1
                if(flag==1):
                    print("NO")
                else:
                    print("YES")
