# https://www.acmicpc.net/problem/1598
# 꼬리를 무는 숫자 나열

# x와 y좌표를 입력 받는다.
x, y = map(int, input().split())

# 좌우 거리는 y를 4로 나눈 몫과 x를 4로 나눈 몫을 뺀 후 절대값 처리,
# 상하 거리는 y를 4로 나눈 나머지와 x를 4로 나눈 나머지를 뺀 후 절대값 처리

# 해답 1 -> 실패 -> 0 부터 시작해야 하는데 1 부터 시작하여서 오~답~
xi = abs((x // 4) - (y // 4)) # |2 - 8| = 6
yi = abs((x % 4) - (y % 4)) # |3 - 1| = 2
print(xi , yi)
print(xi + yi)

# 해답 2 -> 성공
x, y = map(int, input().split())
# if 조건이 참이 아니면 +1 을 해주어야 한다.
xi = abs((x // 4 if x % 4 == 0 else x // 4 + 1) - (y // 4 if y % 4 == 0 else y // 4 + 1))
yi = abs((4 if x % 4 == 0 else x % 4) - (4 if y % 4 == 0 else y % 4))
         
print(xi + yi)
