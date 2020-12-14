# https://www.acmicpc.net/problem/1712

i, j, k = map(int, input().split())

if j>=k:
    print(-1)
else:
    print(int(i/(k-j)+1))