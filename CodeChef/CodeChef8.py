a=int(input())
for i in range(0,a):
    x=int(input())
    b=input()
    if(b.count('I')>0):
        print("INDIAN")
    elif(b.count('Y')>0):
        print("NOT INDIAN")
    else:
        print("NOT SURE")
