# https://www.acmicpc.net/problem/2443
# 별찍기 6

n = int(input())

for i in range(n):
    print(' ' * i, end='')
    print('*' * (( n * 2) - (i * 2 + 1)))