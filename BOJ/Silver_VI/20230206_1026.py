# 1026번

n = int(input())

aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

sortedA = sorted(aList, reverse=True)
sortedB = sorted(bList)

s = 0
for i in range(n):
    s += aList[i] * bList[i]

print(s)