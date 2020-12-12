# https://www.acmicpc.net/problem/2914

# 저작권 = 멜로디 개수 / 앨범 수록곡

# (수록곡 * (저작권-1) + 1) = 멜로디 개수

n , m = map(int,input().split())
print(n * (m-1) + 1)