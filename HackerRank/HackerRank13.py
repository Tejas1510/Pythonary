n=int(input())
a=[31,29,31,30,31,30,31,31,30,31,30,31]
b=[31,28,31,30,31,30,31,31,30,31,30,31]
count=0
if(n%400==0 or (n%4==0 and n%100!=0)):
    i=0
    while(count==256):
        count=count+a[i]
        i=i+1
    print(i)
