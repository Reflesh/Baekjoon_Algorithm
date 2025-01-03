triangle_len = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    plus = triangle_len[i - 3] + triangle_len[i - 2]
    triangle_len.append(plus)
    
T = int(input())
for _ in range(T):
    N = int(input())
    print(triangle_len[N])