# 입력 시간 때문에 input()이 아닌 sys.stdin.readline 사용
import sys

# 입력 받을 숫자의 수 1 ~ 100,000
n = int(input())

# sort를 위한 리스트
num = []

# 들어온 n 값 만큼 저장
for _ in range(n):
    num.append(int(sys.stdin.readline()));

# num 값을 다 저장하고 정렬
num.sort()

for i in num:
    print(i)