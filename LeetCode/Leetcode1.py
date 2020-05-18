def solution(s,t):
    table = {}
    for i in range(len(s)):
    	if(s[i] in table and table[s[i]] != t[i]):
    		return False
    	elif(s[i] not in table and t[i] in table.values()):
            return False
    	else:
            table[s[i]] = t[i]
            print(table[s[i]])
    return True

s=input()
t=input()
result=solution(s,t)
print(result)
