import sys

n = int(input())
sangCard = set(map(int, sys.stdin.readline().split()))

m = int(input())
chkCard = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if chkCard[i] in sangCard:
        print('1', end=' ')
    else:
        print('0', end=' ')