import sys
# 받을 사용자 수
n = int(input());

# 담을 유저 리스트
userList = [];

# 리스트에 맵 형태로 저장
for _ in range(n):
    age, name = map(str, sys.stdin.readline().split())
    userList.append((int(age), name));

# 람다 형식으로 정렬
userList.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(userList[i][0], userList[i][1])