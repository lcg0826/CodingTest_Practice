import sys

def hap(n, time_list):
    result = 0;
    time_list.sort();

    for i in range(n):
        result += time_list[i]*n
        n -=1;

    return print(result);

n = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split()));

hap(n, time_list)

