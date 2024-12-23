# 첫 번째 코드(permutations 사용)
# from itertools import permutations

# num, length = map(int, input().split())
# sequences = list(permutations(range(1, num + 1), length))

# for i in range(len(sequences)):
#     print(*sequences[i])

# 두 번째 코드(백트래킹 기법 사용)
def generate_sequences(num, length):
    result = []
    def backtrack(curr_seq):
        if len(curr_seq) == length:
            result.append(curr_seq.copy())
            return
        for i in range(1, num+1):
            if i not in curr_seq:
                curr_seq.append(i)
                backtrack(curr_seq)
                curr_seq.pop()

    backtrack([])
    return result

num, length = map(int, input().split())
sequences = generate_sequences(num, length)
for i in range(len(sequences)):
    print(*sequences[i])
