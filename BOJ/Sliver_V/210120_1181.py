# https://www.acmicpc.net/problem/1181
# 단어저ㅏㅇ렬

num = int(input())

word_list = []

for _ in range(num):
    word_list.append(input())

word_list_set = list(set(word_list))

# 데이터 타입을 set으로 하였더니
# AttributeError: 'set' object has no attribute 'sort'
# 에러 발생 word_list_set을 중복제거 후 다시 list로 저장
word_list_set.sort(key=lambda i: (len(i), i))

for sorted_word in word_list_set:
    print(sorted_word)

# print(word_list_set)