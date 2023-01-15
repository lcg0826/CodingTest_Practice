import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n) :
    array = sys.stdin.readline().strip().split()

    if len(array) == 1:
        if array[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    else:
        calc, x = array[0], array[1]
        x = int(x)

        if calc == "add":
            s.add(x)
        elif calc == "remove":
            s.discard(x)
        elif calc == "check":
            print(1 if x in s else 0)
        elif calc == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)