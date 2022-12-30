# https://www.acmicpc.net/problem/1316
# 그룹 단어 체커

# 입력 받을 단어 수 n
n = int(input());

# 입력 받은 단어 수 만큼 for문
for i in range(n):
    # word 입력 받은 단어
    word = input();

    # 입력 받은 단어의 개수에서 -1까지 for문
    for j in range(0, len(word)-1):
        # 입력 받은 단어의 j번째와 j+1 번째와 다른 경우
        if word[i] != word[i+1]:
            # 입력 받은 단어의 j번째 알파벳이 j+1번째부터 마지막 안에 동일한 알파벳이 존재하면 그룹문자가 아니기 때문에 -1
            if word[j] in word[j+1:] :
                n -= 1;

print(n)