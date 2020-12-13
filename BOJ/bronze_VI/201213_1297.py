# https://www.acmicpc.net/problem/1297

a, b, c = map(int, input().split())
r = a / ((b ** 2 + c ** 2) ** 0.5)
print(int(b * r), int(c * r))
