def solve(n, result):
    global max_value
    global min_value
    if n == N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    else:
        if operator[0]:
            operator[0] -= 1
            solve(n + 1, result + num[n])
            operator[0] += 1
        if operator[1]:
            operator[1] -= 1
            solve(n + 1, result - num[n])
            operator[1] += 1
        if operator[2]:
            operator[2] -= 1
            solve(n + 1, result * num[n])
            operator[2] += 1
        if operator[3]:
            operator[3] -= 1
            if result < 0 or num[n] < 0:
                solve(n + 1, -(abs(result) // abs(num[n])))
            else:
                solve(n + 1, result // num[n])
            operator[3] += 1
        
N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_value, min_value = -1000000000, 1000000000

solve(1, num[0])
print(max_value)
print(min_value)