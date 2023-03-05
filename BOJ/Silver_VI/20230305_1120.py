import sys

a, b = sys.stdin.readline().split()

result = len(a)

for i in range(len(b) - len(a) + 1):
    cnt = 0
    #A와 문자열 비교
    for j in range(len(a)):
        if a[j]!=b[i+j]:
            cnt += 1

        if cnt > result:
            break

    result = min(result, cnt)

print(result)