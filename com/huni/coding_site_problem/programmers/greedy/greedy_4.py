# https://programmers.co.kr/learn/courses/30/lessons/42885

# 구명 보트

# 문제 설명
# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
#
# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이
#
# 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
#
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
#
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# people	limit	return
# [70, 50, 80, 50]	100	3
# [70, 80, 50]	100	3


####################################################################################################
# 내 풀이
# 구명보트는 작아서 한 번에 최대 2명!! 이게 컸음
# 최대한 작은 것과 최대한 큰것을 넣어서 limit에 가까운숫자대로 집어넣어야할듯?? 이라는 생각
# 1. sorting 후 list에 넣어서 오른쪽에서 하나씪 처내면서 맨 왼쪽의 값과 비교하여 limit 보다 적은 경우 왼쪽 값도 지워나가는 형식으로 해결
# 2. list를 사용하니 pop(0) 에서 타임아웃이 나는것 같아 deque library 사용 후 해결
####################################################################################################

import collections
def solution(people, limit):
    answer = 0

    sort_list = collections.deque(sorted(people))

    while len(sort_list) > 0:
        temp = sort_list.pop()
        answer += 1

        if len(sort_list) >= 1 and temp + sort_list[0] <= limit:
            sort_list.popleft()

    return answer

print(solution([70, 50, 80, 50], 100))

# 다른 사람 풀이

# def solution(people, limit) :
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer