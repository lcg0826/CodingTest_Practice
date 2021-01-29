# https://www.acmicpc.net/problem/1546
# 평균

n = int(input())
num = list(map(int, input().split()))
num_max = max(num)
 
for i in range(n):
    num[i] = num[i]/num_max * 100
avg = sum(num)/ n
print("%.2f" % avg)