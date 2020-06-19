""""""""""""""""""""""""""""""""""""""
Name of Question:Ada and crayons
Link of Question:https://www.codechef.com/problems/ADACRA
"""""""""""""""""""""""""""""""""""""""
for _ in range(int(input())):
    a=input()
    a=a.upper()
    cd=a.split('D')
    cu=a.split('U')
    cD,cU=0,0
    for i in cd:
        if i!='':
            cD+=1
    for i in cu:
        if i!='':
            cU+=1
    print(min(cD,cU))
