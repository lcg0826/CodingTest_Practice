# 크로아티아 알파벳 리스트
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 입력받을 단어
word = input();

# 크로아티아 알파벳 리스트에서 하나씩 뽑아서
# word 안에 크로아티아 알파벳 리스트에서 뺀 i가 속해있다면 치환
for i in alphabet:
    word = word.replace(i, '*')
print(len(word))