n,t=map(int,input().split())
s=input()
a=list(s)
b=sorted(a)

while(t==0):
        for i in range(len(a)-1):
            if(a[i]=="B" and a[i+1]=="G"):
                a[i]="G"
                a[i+1]="B"
                i=i+1
        t=t-1
s="".join(a)
print(s)
