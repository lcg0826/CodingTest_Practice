# https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=pjhLPJV9SHCp
# 다리 놓기

import math

num = int(input())

for _ in range(num):
    n, m = map(int, input().split())
    put_load = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(put_load)