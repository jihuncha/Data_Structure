# https://programmers.co.kr/learn/courses/30/lessons/43165

# 타겟 넘버

# 문제 설명
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
# 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.


# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [2,3,4,5]


# 전체 경우의수 를 구해야하나??

#############################
# 전체 탐색으로 수행
# 하나씩 + , - 적용 시켜주면서 수행
# dfs
#############################

def solution(numbers, target):
    result_list = []

    def dfs_all(index:int, my_list):
        if index > len(numbers) - 1:
            return

        if sum(my_list) == target:
            if my_list[:] not in result_list:
                result_list.append(my_list[:])

        my_list[index] = -my_list[index]

        if sum(my_list) == target:
            if my_list[:] not in result_list:
                result_list.append(my_list[:])

        # print(my_list)
        dfs_all(index+1, my_list)

        my_list[index] = -my_list[index]

        dfs_all(index + 1, my_list)

    dfs_all(0, numbers)

    # print(result_list)
    return len(result_list)

print(solution([1,1,1,1,1] ,3))


# 다른 사람 풀이
########################
# 이게된다고?ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# 근데 이렇게하면 숫자가 어떻게 올라가는거지?
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        # print(solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0]))
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

print(solution([1,1,1,1,1] ,3))

######################
# product가 뭘까??
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


######################
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer