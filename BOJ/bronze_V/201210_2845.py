# https://www.acmicpc.net/problem/2845

n, m = map(int, input().split())
people = list(map(int, input().split()))

accpeople = n * m

for p in people:
    print(p - accpeople , end = ' ')

