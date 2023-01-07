import sys

# 점의 개수 N
N = int(input())
# 좌표 리스트
pointList = []

# x, y 좌표를 pointList에 추가
for _ in range(N):
    xPoint, yPoint = map(int, sys.stdin.readline().split())
    pointList.append([yPoint, xPoint])

# 정렬    
pointList.sort()

# poinstList 길이만큼 돌려서 배열 값 출력
for i in range(len(pointList)):
    print(pointList[i][1], pointList[i][0])
    