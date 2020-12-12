# https://www.acmicpc.net/problem/3003


# a, b, c, d, e, f = 1, 1, 2, 2, 2, 8
chess = [1, 1, 2, 2, 2, 8]
n = list(map(int, input().split()))

for i in range(len(n)):
    print(chess[i] - n[i], end = ' ')