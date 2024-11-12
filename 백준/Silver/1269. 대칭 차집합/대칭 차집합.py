A_num, B_num = map(int, input().split())
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

A_B = A_set - B_set
B_A = B_set - A_set

print(len(A_B) + len(B_A))