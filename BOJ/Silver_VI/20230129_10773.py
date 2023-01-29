import sys
def hap(k):

    for num in range(k):
        n = int(sys.stdin.readline())
        if n == 0:
            stk.pop();
        else:
            stk.append(n);

    return print(sum(stk));


stk = [];
k = int(sys.stdin.readline())

hap(k);