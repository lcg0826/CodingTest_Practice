# https://www.acmicpc.net/problem/1247
# 분산처리

# 해당 코드는 오류가 존재
# 주어진 문제 조건에 따르면 10번인 경우는 10이 출력되어야 
# 하지만 아래 코드에는 10으로 나눈 나머지가 0이 나오는 경우가 발생 
'''
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print((a**b) % 10)
'''


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    # 1의 자리 수가 4와 9인 경우는 반복 되는 값이 2개 이므로 제곱수를 2로 나누어서
    # 홀수 승과 짝수 승을 비교하여 계산
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
    # 4개씩 싸이클이 돌 때 마다 자기 자신이 나오므로 나누었을때 나머지가 0이라면 자기 자신을 출력
        b = b % 4
        if b == 0:
            print((a ** 4 ) % 10 )
        else:
            print((a ** b) % 10)
            
