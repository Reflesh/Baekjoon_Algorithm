import sys
input = sys.stdin.readline
import math as m

def sol(k):
    if int(m.sqrt(k)) == m.sqrt(k):
        return 1
    for i in range(1, int(m.sqrt(k))+1):
        if int(m.sqrt(k-i**2)) == m.sqrt(k-i**2):
            return 2
    for i in range(1, int(m.sqrt(k))+1):
        for j in range(1, int(m.sqrt(k-i**2))+1):
            if int(m.sqrt(k-i**2-j**2)) == m.sqrt(k-i**2-j**2):
                return 3
    return 4

num = int(input())
print(sol(num))