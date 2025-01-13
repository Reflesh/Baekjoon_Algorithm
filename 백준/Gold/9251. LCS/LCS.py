first_ch = list(input())
second_ch = list(input())
result = []

for i in range(len(first_ch) + 1):
    row = [0] * (len(second_ch) + 1)
    result.append(row)

# print(first_ch)
# print(second_ch)
# print(result)

for i in range(1, len(first_ch) + 1):
    for j in range(1, len(second_ch) + 1):
        if first_ch[i-1] == second_ch[j-1]:
            result[i][j] = result[i-1][j-1] + 1 # LCS 길이 저장
        else:
            result[i][j] = max(result[i-1][j], result[i][j-1]) # LCS의 길이 최댓값 저장

# print(result)
print(result[len(first_ch)][len(second_ch)])