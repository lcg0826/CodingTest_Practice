n , m = map(int,input().split())
nList = set()
mList = set()

for _ in range(n):
    nList.add(input())
for _ in range(m):
    mList.add(input())

arr = sorted(list(nList & mList))
print(len(arr))

for i in arr:
    print(i)