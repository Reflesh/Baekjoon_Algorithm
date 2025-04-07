import sys
input = sys.stdin.readline

def fibonacci(num):
    for i in range(2, num+1):
        if zero_count[i] == -1:
            zero_count[i] = zero_count[i-1] + zero_count[i-2]
            one_count[i] = one_count[i-1] + one_count[i-2]
        
case_num = int(input())
zero_count = [1, 0] + [-1] * 39
one_count = [0, 1] + [-1] * 39
for _ in range(case_num):
    N = int(input())
    fibonacci(N)
    print(zero_count[N], one_count[N])