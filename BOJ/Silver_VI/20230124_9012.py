num = int(input())
for i in range(num):
    ch = input()
    res = list(ch)
    sum = 0
    for i in res:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')