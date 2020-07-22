n=int(input())
s=input()
sum=0
a=[int(i) for i in s]
for i in range(len(a)):
    if(a[i]%2==0):
        sum=sum+i+1
print(sum)
