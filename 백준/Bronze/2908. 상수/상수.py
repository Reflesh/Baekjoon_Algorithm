s, t = input().split()
s = int(s[::-1])
t = int(t[::-1])

if s > t:
    print(s)
else:
    print(t)