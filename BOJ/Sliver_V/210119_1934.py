# https://www.acmicpc.net/problem/1934
# 최소공배수

def min(n, m):
    result = max(n, m)
    return result * (n // result) * (m // result)
def max(n, m):
    return max(m % n, n) if m % n else n

num = int(input())
for i in range(num):
    num1, num2 = map(int, input().split())
    print(min(num1, num2))
    