A = [3, 4, 5, 3, 7]
A = [1, 2, 3, 4]
A = [1, 3, 1, 2]

def solution(A:list):
    # write your code in Python 3.6

    # 결과 count
    result_count = 0

    # nextCheck가 이전과 동일한 경우 return false, 모두 다른 경우 return true
    # nextCheck - 이전값이 다음값보다 적은 경우 1 // 이전 값이 다음값보다 큰 경우 0
    def checkUpDownList(data:list):
        nextCheck = -1

        for i in range(len(data) - 1):
            if data[i] < data[i+1]:
                if nextCheck == 1:
                    return False
                nextCheck = 1
            elif data[i] > data[i+1]:
                if nextCheck == 0:
                    return False
                nextCheck = 0
        return True

    # 이미 aesthetically pleasing인 경우
    if checkUpDownList(A):
        return result_count

    # 아닌 경우 하나씩 제거하면서 체크한다.
    for i in range(len(A)):
        temp_list = A[:]
        del temp_list[i]
        # aesthetically pleasing인 경우 count를 올려준다,
        if checkUpDownList(temp_list):
            result_count += 1

    return result_count if result_count > 0 else -1

    pass

print(solution(A))