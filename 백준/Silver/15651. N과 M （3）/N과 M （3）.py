def generate_sequences(num, length):
    result = []
    def backtrack(curr_seq):
        if len(curr_seq) == length:
            result.append(curr_seq.copy())
            return
        for i in range(1, num+1):
            curr_seq.append(i)
            backtrack(curr_seq)
            curr_seq.pop()

    backtrack([])
    return result

num, length = map(int, input().split())
sequences = generate_sequences(num, length)
for res in sequences:
    print(*res)