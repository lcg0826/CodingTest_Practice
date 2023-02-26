import sys

n, k, l = map(int, sys.stdin.readline().split())
count = 0

while k != l:
    k -= k // 2
    l -= l // 2
    count += 1 # 카운트

print(count)