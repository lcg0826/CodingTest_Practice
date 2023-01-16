# 붙일 길이
x = int(input())
cnt = 0
# 자르고 남는 길이
n = 64

while x > 0:
    if n > x:
        n = n // 2
    else:
        cnt += 1
        x -= n
print(cnt)