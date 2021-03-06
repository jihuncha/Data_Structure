# https://programmers.co.kr/learn/courses/30/lessons/43238

# 입국 심사

# n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
#
# 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다.
#
# 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
#
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
#
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가
#
# 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.

# 입출력 예
# n	times	return
# 6	[7, 10]	28
#
# 입출력 예 설명
# 가장 첫 두 사람은 바로 심사를 받으러 갑니다.
#
# 7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
#
# 10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
#
# 14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
#
# 20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.

###########
# 10억명 10억분이 말이냐
# 해결방안이 모색안되서 답보고..ㅠ


###############################
# 문제의 핵심은 최소, 최대 범위를 구한 뒤 구하려고 하는 답을 이분 탐색으로 범위를 좁혀가며 답을 구하는 것 입니다.
#
# 문제에서 최대 범위는 심사관 중 가장 오래걸리는 심사관을 계속 검사 받는 경우입니다.
# 최소, 최대 범위의 중간값인 mid가 n명을 심사 할 수 있는 지 아닌 지를 파악하며 이분 탐색을 진행합니다.
#
# n명을 심사 할 수 있다면, 답을 갱신하고, 최대 범위를 줄여봅니다.
# n명을 심사 할 수 없다면, 최소범위를 늘려봅니다.


# https://wwlee94.github.io/category/algorithm/binary-search/immigration/
# https://codingspooning.tistory.com/78

# 6 -[ 7 , 10]
def solution(n, times):
    answer = 0

    left = 1
    right = max(times) * n

    print(left,right)

    while left <= right:
        mid = (left + right) // 2
        print('mid - ', mid)
        count = 0
        # 주어진 시간안에 심사위원이 몇명 심사 할수 있는지 카운트하는 것
        for time in times:
            count += mid // time
        print("count = ", count)

        # 모든 사람이 심사 가능한 경우
        # answer에 저장한다.
        # mid 줄여본다
        if count >= n:
            answer = mid
            right = mid - 1
        # mid 늘려본다.
        else:
            left = mid + 1
        print("left and right = ", left,right)

    return answer

print(solution(6,[7, 10]))





