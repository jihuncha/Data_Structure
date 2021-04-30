# https://leetcode.com/problems/number-of-islands/

# Example 1:
#
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# Output: 3
from typing import List


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:


################################################################################################
#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Example 1:
#
digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# digits = ""
# Output: []
# Example 3:
#
# digits = "2"
# Output: ["a","b","c"]


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#
#         def dfs(index, str_result):
#             if len(digits) == len(str_result):
#                 result.append(str_result)
#                 return
#
#             for check in range(index, len(digits)):
#                 for i in dic[digits[check]]:
#                     dfs(check + 1, str_result + i)
#
#         dic = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl",
#                "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
#         result = []
#         dfs(0,"")
#         return result
#
# print(Solution().letterCombinations(digits))

###################################################
#https://leetcode.com/problems/permutations/

# Example 1:
#
nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# nums = [1]
# Output: [[1]]

import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(nums))
        if not nums:
            return [[]]

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                print("e - ", e)
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                # print(prev_elements)

        result = []
        prev_elements = []

        dfs(nums)
        return result
print(Solution().permute(nums))