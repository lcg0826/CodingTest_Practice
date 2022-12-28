# https://www.acmicpc.net/problem/4673
# 셀프 넘버
# 여기서 생성자가 없는 숫자들은
# 1 -> 1+1 = 2                  8 -> 8+8 = 16
# 2 -> 2+2 = 4                  9 -> 9+9 = 18
# 3 -> 3+3 = 6                 10 -> 10 + 1 + 0 = 11
# 4 -> 4+4 = 8                 11 -> 11 + 1 + 1 = 13
# 5 -> 5+5 = 10                12 -> 12 + 1 + 2 = 15
# 6 -> 6+6 = 12                13 -> 13 + 1 + 3 = 17
# 7 -> 7+7 = 14                14 -> 14 + 1 + 4 = 19
# 위와 같이 중간에 만들어지지 않는 숫자가 생성자가 없는 숫자이다.


# calNum 함수 : 받은 숫자 i와 i의 각 자리수를 합하고 return;
def calNum(i):
    return i + sum(map(int, str(i)));

# setNum은 문제에서 주어진 10000이하의 숫자까지 계산
setNum = set(range(1, 10001));

# constNum : 생성자가 있는 숫자
constNum = set();

# 생성자가 있는 숫자를 추가
for n in range(1, 10001):
    constNum.add(calNum(n))

# 10000이하의 숫자 항목 - 생성자가 있는 숫자 항목 = 생성자가 없는 숫자 항목
for m in sorted(setNum - constNum):
    print(m);
