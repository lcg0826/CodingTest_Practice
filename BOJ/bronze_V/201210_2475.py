# https://www.acmicpc.net/problem/2475

# 방법 1
# a, b, c, d, e = map(int, input().split())

## 각 제곲들의 핪을 10으로 나눈 나머지 값  출력
# print(((a**2) + (b**2) + (c**2) + (d**2) + (e**2)) % 10)

# 방법 2
list1 = list(map(int,input().split()))

hap = 0

for l in list1:
    hap += l**2

print(hap%10)