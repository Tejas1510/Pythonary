t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    for i in range(len(a)):
        if(a[i]%2==0):
            flag=1
            index=i
            break
    if(flag==1):
        print(1)
        print(i+1)
    else:
        try:
            for i in range(len(a)):
                for j in range(1,len(a)):
                    if((a[i]+a[j])%2==0):
                        print(2)
                        print(i+1,j+1)
                        break
                break        
            else:
                print(-1)
        except:
            print(-1)
