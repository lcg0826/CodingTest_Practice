# https://www.acmicpc.net/problem/2455
# 지능형 기차

result = 0
maxresult = 0
for i in range(4):
    n, m = map(int, input().split())
    result -= n
    result += m
    maxresult = max(maxresult, result)
print(maxresult)