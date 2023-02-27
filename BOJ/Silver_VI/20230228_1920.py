n = int(input())
nArray = set(map(int,input().split()))
m = int(input())
mArray = list(map(int,input().split()))

for i in mArray:
    if i not in nArray:
        print('0')
    else:
        print('1')