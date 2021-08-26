# https://programmers.co.kr/learn/courses/30/lessons/43164

# 여행 경로

# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
#
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

# 입출력 예
# tickets	return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# 입출력 예 설명
# 예제 #1
#
# ["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.
#
# 예제 #2
#
# ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.


def check_dfs(start: str, dic_info: dict, result_list: list):
    global result_all
    global count

    if start not in dic_info:
        return

    # print([x for x in dic_info[start]])
    my_list = sorted([x for x in dic_info[start]])
    result_list.append(start)
    count -= 1
    # print(count)

    if count == 0:
        result_list.append(dic_info[start][0])
        # result_all.append(result_list[:])
        result_all = result_list[:]

    for i in range(len(my_list)):
        temp = my_list[i]
        # print(temp)
        dic_info[start].remove(temp)
        check_dfs(temp, dic_info, result_list)
        # 백트래킹
        dic_info[start].append(temp)
        dic_info[start].sort()
        # count += 1


def solution(tickets):
    answer = []

    dic = {}

    for i in tickets:
        if i[0] not in dic:
            dic[i[0]] = [i[1]]
        else:
            dic[i[0]].append(i[1])

    global result_all
    global count

    count = len(tickets)
    result_all = []

    check_dfs('ICN', dic, [])

    # print("result - ", temp_result)
    # print(result_all)

    # temp_list = sorted([x for x in dic['ICN']])
    # print(temp_list)
    #
    # for i in temp_list:
    #     dic[]
    #
    # # queue = deque(sorted([x for x in dic['ICN']]))
    # # print(queue)
    # #
    # # while queue:
    # #     temp = queue.popleft()
    # #     result_list = sorted([x for x in dic[temp]])

    return result_all

# print(solution( [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))
# ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]

# temp_list = ['a','b','c']
# temp_list.remove('a')
# print(temp_list)

# 테스트 1 〉	실패 (159.26ms, 11.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)

# params: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
# return: ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

# [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
# ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]

# https://gurumee92.tistory.com/165