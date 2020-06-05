""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and his Sequence
Link of Question:https://www.codechef.com/problems/CHEFSQ
"""""""""""""""""""""""""""""""""""""""
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    t=list(map(int,input().split()))
    if m>n:
        print("No")
    else:
        c=0
        for i in l:
            if i==t[c]:
                c +=1
                if c==m:
                    break

        if c>=m:
            print("Yes")
        else:
            print("No")
