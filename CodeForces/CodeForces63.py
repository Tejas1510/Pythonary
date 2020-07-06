n=int(input())
if(n%2==0):
    print((n**2)//2)
else:
    print((n**2+1)//2)
a=[["."]*n]*n
for i in range(n):
    for j in range(n):
        if(i%2==0):
            if(j%2==0):
                a[i][j]="C"
                print(a[i][j],end="")

            else:
                a[i][j]="."
                print(a[i][j],end="")
        else:
            if(j%2!=0):
                a[i][j]="C"
                print(a[i][j],end="")
            else:
                a[i][j]="."
                print(a[i][j],end="")
    print("")
# for i in range(n):
#     for j in range(n):
#         print(a[i][j],end="")
#     print("")
