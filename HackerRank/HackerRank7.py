 Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]

n=int(input())

e=[]
for i in range(0,n+1):
    count1=0
    c=bin(i).replace("0b","")
    d=list(str(c))
    for i in range(0,len(d)):
        d[i]=int(d[i])
        if(d[i]==1):
            count1=count1+1
    e.append(count1)
print(e)
