n, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
num_list.reverse()

print(num_list[k - 1])