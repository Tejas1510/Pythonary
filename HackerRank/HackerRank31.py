n,k=[int(temp) for temp in input().strip().split()]
s=[int(temp)%k for temp in input().strip().split()]
print(s)
remainder=[0]*k
for x in s:
    remainder[x]+=1
    print(remainder)
