""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Minimum changes to make all substrings distinct
Link of Question:https:https://practice.geeksforgeeks.org/problems/minimum-changes-to-make-all-substrings-distinct/0
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=input()
    n1=len(n)
    n2=len(list(set(n)))
    print(abs(n2-n1))
