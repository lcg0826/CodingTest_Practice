import sys

num = int(sys.stdin.readline())

cnt = 0;
while num >= 5:
    cnt += num // 5
    num //= 5;

print(cnt);
