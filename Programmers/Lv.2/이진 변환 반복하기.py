def solution(s):
    answer = []
    result_cnt = 0
    result_remove_zero_cnt = 0

    while s != '1':
        # 0의 개수
        zero_cnt = s.count('0')
        # 입력받은 s값 - 0의 개수
        # [2:] 의미 : 10진법 -> 2진법으로 치환할 경우 진법 표시 제거
        s = bin(len(s) - zero_cnt)[2:]
        # 2진 변환 횟수
        result_cnt += 1
        # 제거된 0의 개수 누적
        result_remove_zero_cnt += zero_cnt


    return [result_cnt, result_remove_zero_cnt]