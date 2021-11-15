# https://leetcode.com/problems/reconstruct-itinerary/

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight.
# Reconstruct the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK",
# thus, the itinerary must begin with "JFK". If there are multiple valid itineraries,
# you should return the itinerary that has the smallest lexical order when read as a single string.
#
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
import collections
import copy

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

# Output: ["JFK","MUC","LHR","SFO","SJC"]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

# Constraints:
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi


# Input
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# Output
# ["JFK","KUL"]
# Expected
# ["JFK","NRT","JFK","KUL"]

# 시간초과
# tickets = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]

from typing import List

## 시간초과..
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dictionary 생성
        dic = {}
        for i in tickets:
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
            else:
                dic[i[0]].append(i[1])

        # print(dic)

        # 결과를 담을 list
        result_list = []

        # key 값, 변경된 dic 값, 결과를 담는 list
        def dfs(val_key:str, val_dic:dict, temp_result_list:list):
            # 다음 키가 없는 경우
            if val_key not in val_dic or len(val_dic[val_key]) == 0:
                # 길이가 만족하는 경우면 결과값에 더해준다
                if len(temp_result_list) == len(tickets) + 1:
                    result_list.append(temp_result_list[:])
                return

            # 길이가 만족하는 경우 결과값에 더해준다
            if len(temp_result_list) == len(tickets) + 1:
                result_list.append(temp_result_list[:])

            for i in range(len(val_dic[val_key])):
                # 임시로 dictionary에서 하나 추출
                temp = val_dic[val_key].pop(i)
                # dfs 추가로 돌려줄 list생성하고 value 담아준다
                mak_new_result = temp_result_list[:]
                mak_new_result.append(temp)
                
                dfs(temp, val_dic, mak_new_result)
                # 백트래킹
                val_dic[val_key].insert(i, temp)

        dfs('JFK', dic, ['JFK'])

        result_list.sort()

        return result_list[0] if len(result_list) > 0 else []

# 풀이 1
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dictionary 생성
        dic = collections.defaultdict(list)
        dic_temp = {}
        print(dic)
        for i in sorted(tickets):
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
                dic_temp[i[0]] = [i[1]]
            else:
                dic[i[0]].append(i[1])
                dic_temp[i[0]].append(i[1])

        print(dic)
        print(dic_temp)

        result_list = []

        def dfs(a):
            while dic[a]:
                dfs(dic[a].pop(0))
            result_list.append(a)

        dfs('JFK')
        return result_list[::-1]



# 풀이 2 - pop(0) 이 O(n) 만큼 시간이 걸리므로 pop() 사용하기 위해 reverse 사용
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dictionary 생성
        dic = collections.defaultdict(list)
        dic_temp = {}

        #reverse
        for i in sorted(tickets, reverse=True):
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
                dic_temp[i[0]] = [i[1]]
            else:
                dic[i[0]].append(i[1])
                dic_temp[i[0]].append(i[1])

        result_list = []

        def dfs(a):
            while dic[a]:
                # pop
                dfs(dic[a].pop())
            result_list.append(a)

        dfs('JFK')
        return result_list[::-1]

# 풀이 3 - 일정 그래프 반복
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # print(tickets)
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        print(graph)

        # 이해가 잘안가네..
        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        # 다시 뒤집어 어휘순 결과로
        return route[::-1]



print(Solution().findItinerary(tickets))