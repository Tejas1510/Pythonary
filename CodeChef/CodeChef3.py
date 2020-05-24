test=int(input())
for i in range (0,test):
    x=int(input())
    if (x!=2 and x>0 and x!=1):
        print(x**3-(x-2)**3)
    else:
        print(x**3)
