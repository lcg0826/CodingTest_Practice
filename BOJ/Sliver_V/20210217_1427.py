# https://www.acmicpc.net/problem/1427
# 소트인사이드


n = list(str(input()))
n.sort(reverse = True)
result = ""

for i in n:
    result += i
print(int(result))