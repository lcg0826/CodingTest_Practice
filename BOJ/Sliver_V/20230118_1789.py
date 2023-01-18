hap = int(input())
tot = 0
cnt = 0

while True:
    cnt += 1
    tot += cnt
    if tot > hap:
        break

print(cnt-1)