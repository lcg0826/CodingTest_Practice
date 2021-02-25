# https://www.acmicpc.net/problem/1259
# 팰린드롬수

while 1:
    text = input()
    if text == '0':
        break
    if text == text[::-1]:
        print('yes')
    else:
        print('no')
        