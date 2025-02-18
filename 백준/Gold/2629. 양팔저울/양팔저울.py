import sys
input = sys.stdin.readline

def sol(num, wg):
    if num > weight_num: # 구슬의 숫자가 더 큰 경우
        return
    if dp[num][wg] == 1: # 이미 연산함
        return
    dp[num][wg] = 1
    
    sol(num + 1, wg + weight[num-1])       # 추 추가하기
    sol(num + 1, wg)                       # 그대로 진행
    sol(num + 1, abs(wg - weight[num-1]))  # 반대편에 추 추가(무게빼기)

weight_num = int(input())
weight = list(map(int, input().split()))
bead_num = int(input())
bead = list(map(int, input().split()))
# dp[사용한 추의 개수][무게 차이]
dp = [[0 for _ in range(500 * weight_num + 1)] for _ in range(weight_num + 1)]

sol(0, 0)

for k in bead:
    if k > 500 * weight_num: # 가능한 구슬 무게 범위 초과
        print("N", end=' ')
    elif dp[weight_num][k]:  # 구슬 무게 측정 가능
        print("Y", end=' ')
    else:                    # 구슬 무게 측정 불가능
        print("N", end=' ')