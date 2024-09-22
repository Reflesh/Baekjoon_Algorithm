n = int(input())
score = list(map(int, input().split()))
max_score = max(score)

score_ = [sc / max_score * 100 for sc in score]
average = sum(score_) / len(score_)
print(average)