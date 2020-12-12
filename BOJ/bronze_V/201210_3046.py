# https://www.acmicpc.net/problem/3046

# R1 * R2 / 2 = S
# 구해야 하는 값는 R2
# S * 2 - R1 = R2
R1, S = map(int, input().split())

print(S * 2 - R1)