# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


nums = [0]
# Output: [[],[0]]

# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


# 내풀이 32ms
from typing import List
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(nums) + 1):
            temp = list(map(list, combinations(nums, i)))
            result += temp

        return result

print(Solution().subsets(nums))

# 책 풀이
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#
#         def dfs(index, path):
#             # 매 번 결과 추가
#             result.append(path)
#
#             # 경로를 만들면서 DFS
#             for i in range(index, len(nums)):
#                 dfs(i + 1, path + [nums[i]])
#
#         dfs(0, [])
#         return result