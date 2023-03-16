def solution(s):
    str_list = list(map(int, s.split(' ')))
    answer = str(min(str_list)) + ' ' + str(max(str_list))
    return answer