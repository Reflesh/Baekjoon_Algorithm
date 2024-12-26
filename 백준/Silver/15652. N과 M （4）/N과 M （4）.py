def generate_sequences(num, length):
    result = []
    def backtrack(curr_seq, start):
        if len(curr_seq) == length:
            result.append(curr_seq.copy())
            return
        for i in range(start, num+1):
            curr_seq.append(i)
            backtrack(curr_seq, i)
            curr_seq.pop()

    backtrack([], 1)
    return result

num, length = map(int, input().split())
sequences = generate_sequences(num, length)
for res in sequences:
    print(*res)