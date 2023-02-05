n, k = map(int,input().split())
result= []
arr = [i for i in range(1, n + 1)]
num = 0
for i in range(n):
    num += (k-1)
    if num >= len(arr):
        num %= len(arr)
    result.append(str(arr[num]))
    arr.pop(num)

print("<",', '.join(result), ">", sep="")