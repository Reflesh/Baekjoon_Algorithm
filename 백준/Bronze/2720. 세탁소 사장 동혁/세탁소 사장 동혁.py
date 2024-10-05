t = int(input())
  
for _ in range(t):
    cent = int(input())
    for i in [25, 10, 5, 1]:
        print(cent // i, end = ' ')
        cent = cent % i
    print()  # 가독성을 위해 작성