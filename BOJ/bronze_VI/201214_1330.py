# https://www.acmicpc.net/problem/1330

n, m = map(int,input().split())

if n > m:
    print('>')
elif n < m:
    print('<')
else:
    print('==')