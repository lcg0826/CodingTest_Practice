def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    print(A)
    print(B)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer