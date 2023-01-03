# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
M = int(input())
N = int(input())

sosu = []
for n in range(M, N+1):
    notSosu = False;
    # 0과 1은 소수가 아니기 때문에 n은 2부터
    if n > 1 :
        # 2부터 n-1까지
        for i in range(2, n):
            # 2부터 n-1까지 나눈 몫이 0이면 for문을 끝냄
            if n % i == 0:
                notSosu = True;
                break
        if notSosu != True:
            sosu.append(n)  # notSosu가 True면 sosu 리스트에 값 추가
if len(sosu) > 0:
    print(sum(sosu));
    print(min(sosu));
else:
    print(-1);