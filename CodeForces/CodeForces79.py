n,t=map(int,input().split())
s=input()
a=list(s)

while(t!=0):
    i=0
    while(i<len(a)-1):
        if(a[i]=="B" and a[i+1]=="G"):
            a[i]="G"
            a[i+1]="B"
            i=i+2
        else:
            i=i+1
    t=t-1
s=""
s="".join(a)
print(s)
