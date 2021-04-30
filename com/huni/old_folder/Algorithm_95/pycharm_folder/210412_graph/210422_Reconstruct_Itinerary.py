from typing import List

# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

# ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # current = tickets[0][0]
        dic = {}
        result = []
        for check in sorted(tickets):
            if check[0] not in dic:
                dic[check[0]] = [check[1]]
            else:
                dic[check[0]].append(check[1])
        print(dic)
        # 재귀형태
        # print(type(dic.values()))
        # print(dic)
        # def dfs(a):
        #     # print(a)
        #     while dic[a]:
        #         print(dic)
        #         dfs(dic[a].pop(0))
        #     # print(result)
        #     result.append(a)
        #
        # dfs('JFK')

        # 번복 형태
        stack = ['JFK']

        count = 0
        while stack:
            while dic[stack[-1]]:
                print(count, " - ", dic[stack[-1]])
                count+=1
                stack.append(dic[stack[-1]].pop(0))
                print("test - " ,stack)
            result.append(stack.pop())
        return result[::-1]

print(Solution().findItinerary(tickets))
