import math

tree = []
tree_interval = []
n = int(input())

for _ in range(n):
    dis = int(input())
    tree.append(dis)
    
for i in range(len(tree) - 1):
    tree_interval.append(tree[i+1] - tree[i])
    
gcd = tree_interval[0]
for i in range(1, len(tree_interval)):
    gcd = math.gcd(gcd, tree_interval[i])
    
cnt = 0
for i in range(len(tree_interval)):
    s = tree_interval[i] // gcd - 1
    cnt += s
    
print(cnt)