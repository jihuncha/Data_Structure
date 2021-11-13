# https://leetcode.com/problems/combinations/

# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
#
# You may return the answer in any order.
from typing import List

n = 4
k = 2

# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

n = 1
k = 1

# Output: [[1]]


# dfs
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result_list = []

        def dfs(temp_list:List, last_list:list):
            if len(temp_list) == k:
                result_list.append(temp_list[:])
                return

            for i in range(len(last_list)):
                # 임시 리스트에 담아준다.
                temp_list.append(last_list[i])
                # 잔여 리스트 생성
                temp = last_list[i+1:]
                # dfs
                dfs(temp_list, temp)
                # 기존 임시 리스트 삭제
                temp_list.remove(last_list[i])

        dfs([], [x for x in range(1,n+1)])

        return result_list

print(Solution().combine(n,k))

# combination

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1,n+1),k)))


print(Solution().combine(n,k))

