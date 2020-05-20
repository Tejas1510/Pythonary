
s = input().strip()
n = int(input().strip())
c = sum(x == 'a' for x in s)
print()
print(c * (n//len(s)) + sum(x == 'a' for x in s[:n%len(s)]))
