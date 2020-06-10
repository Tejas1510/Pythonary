""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Gift
Link of Question:https://www.codechef.com/problems/PRGIFT
"""""""""""""""""""""""""""""""""""""""
for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    l=list(map(int, input().split()))
    count=0
    for i in l:
        if i%2==0:
            count+=1

    if k==0 and count==n:
        print('NO')
    elif count<k:
        print('NO')
    else:
        print('YES')
