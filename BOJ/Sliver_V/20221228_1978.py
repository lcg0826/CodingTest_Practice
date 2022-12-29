# https://www.acmicpc.net/problem/1987

# 받을 숫자 개수
n = int(input());

# 소수인지 확인하려는 숫자 리스트
numberList = list(map(int, input().split()))

sosu = 0;
for i in numberList:
    # 1로 나누는 것은 제외하고
    # 2부터 시작해서 자기 자신으로 나누어 떨어지면 sosu 개수 1 추가하고
    # break으로 빠져나옴
    for j in range(2,i+1):
        if i % j == 0:
            if i == j:
                sosu += 1;
            break;
print(sosu);

