from collections import deque

# 인원수 N 제거할 K 번째 숫자
N, K = map(int, input().split())

deq = deque();

print('<', end='')

# deque에 1부터 N+1까지 append
for i in range(1, N+1):
    deq.append(i);

# deq가 참인 경우
while deq:
    # K-1번까지 뒤에 추가 후 맨 앞 삭제
    for _ in range(K - 1):
        deq.append(deq[0]);
        deq.popleft();
    print(deq.popleft(), end='')
    if deq:
        print(', ', end='')

print('>', end='')
