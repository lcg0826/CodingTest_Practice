# https://www.acmicpc.net/problem/1547
# 공

n = int(input())

cup = [1,2,3]
for _ in range(n):
    x, y = map(int, input().split())
    
# index 함수는 위치 반환을 해줌
    xi = cup.index(x)
    yi = cup.index(y)
    
    cup[xi], cup[yi] = cup[yi], cup[xi]
    
print(cup[0])