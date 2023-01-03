# 입력 받을 사람 수
n = int(input());
peopleList = [];

for _ in range(n):
    w, h = map(int, input().split());
    # 입력 받을 사람 수 n만큼 for문 돌려서 peopleList에 몸무게, 키 저장
    peopleList.append((w, h));

# peopleList에 담은 데이터 값으로 계산
for i in peopleList:
    rank = 1
    for j in peopleList:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1;

    print(rank);