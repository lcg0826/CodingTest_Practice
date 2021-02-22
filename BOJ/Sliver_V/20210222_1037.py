# https://www.acmicpc.net/problem/1037
# 약수

n = int(input())
N = list(map(int, input().split()))

N_max = max(N)
N_min = min(N)

print(N_max * N_min)