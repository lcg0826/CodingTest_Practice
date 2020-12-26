# https://www.acmicpc.net/problem/2440
# 별찍기 3


n = int(input())
for i in range(1, n + 1):
    print("*"*(n - i + 1))