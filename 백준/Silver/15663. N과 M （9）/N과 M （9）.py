import sys
input = sys.stdin.readline

def sol(k):
    if k == length:
        print(*result)
        return

    prev = 0
    for i in range(len(seq)):
        if not visited[i] and seq[i] != prev:
          result.append(seq[i])
          visited[i] = True
          prev = seq[i]
          sol(k+1)
          result.pop()
          visited[i] = False

num, length = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
visited = [False] * num
result = []

sol(0)