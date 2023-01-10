import sys

# 순서대로 지구 수, 태양 수, 달의 수
E, S, M = map(int, sys.stdin.readline().split())

# 지나는 년도
year = 1

while True:
    if(year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1