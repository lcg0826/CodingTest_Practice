import sys
def hap(n, k):
    result = 0;
    coin = [];

    for i in range(n):
        m = int(sys.stdin.readline())
        coin.append(m);

    coin.reverse();

    for i in range(n):
        if coin[i] > k:
            continue;
        else:
            result += k // coin[i]
            k = k - ((k // coin[i]) * coin[i])

    return print(result);

n, k = map(int, sys.stdin.readline().split())
hap(n, k);
