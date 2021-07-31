def chooseandswap(A):
    temp = ' '
    for i in range(len(A)):
        for j in range(len(A)-2):
            if A[j] > A[j+1]:
                temp=A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    answer = ""
    for i in range(len(A)):
        answer += A[i]
    return answer

word = ['c','c','a','d']
print(chooseandswap(word))
