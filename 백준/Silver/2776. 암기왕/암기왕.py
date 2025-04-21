import sys
input = sys.stdin.readline

def binary_search(low, high, find):
    
    while low <= high:
        mid = (low + high) // 2
        if note1_info[mid] == find:
            return 1
        elif note1_info[mid] < find:
            low = mid + 1
        else:
            high = mid - 1
    return 0

test_case = int(input())
for _ in range(test_case):
    note1_num = int(input())
    note1_info = list(map(int, input().split()))
    note1_info.sort()
    
    note2_num = int(input())
    note2_info = list(map(int, input().split()))
    
    for f in note2_info:
        print(binary_search(0, note1_num - 1, f))