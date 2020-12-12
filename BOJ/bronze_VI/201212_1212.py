# https://www.acmicpc.net/problem/1212

# 정수형을 8진수로 입력 받기
n = int(input(), 8)

# 받은 입력값을 bin 함수를 통해 2진수로 변환
n = bin(n)

# 해당 문제에선 1부터 출력 되도록함
# print(n)을 실행하면 결과값은 0b11001100 가 출력되므로 슬라이싱 처리를 해줌
print(n[2:])