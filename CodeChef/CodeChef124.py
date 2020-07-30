t=int(input())
for i in range(t):
    n=int(input())
    b=""
    for i in range(n):
        s=input()
        b=b+s

    c=b.count("c")
    e=b.count("e")
    o=b.count("o")
    d=b.count("d")
    h=b.count("h")
    f=b.count("f")
    if(c<2 or e<2):
        print(0)
    elif(o<1 or d<1 or h<1 or f<1 ):
        print(0)
    else:
        print(min((min(c,e)//2),min(o,f,d,h)))
