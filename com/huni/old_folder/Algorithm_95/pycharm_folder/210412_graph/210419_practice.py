from typing import List

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
# #
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         def dfs(x,y):
#             if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
#                 return
#
#             grid[x][y] = '0'
#
#             dfs(x + 1, y)
#             dfs(x - 1, y)
#             dfs(x, y + 1)
#             dfs(x, y - 1)
#
#         count = 0
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if grid[x][y] == '1':
#                     dfs(x,y)
#
#                     count+=1
#
#         dfs(0,0)
#
#         return count
#
#
#
#
# print(Solution().numIslands(grid))


# temp = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
#
# print(temp[3][4])
# print(len(temp))
# print(len(temp[0]))

# Example 1:

digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        result = []

        def dfs(index, str_temp):
            if len(digits) == len(str_temp):
                result.append(str_temp)
                return

            for i in range(index, len(digits)):
                for temp_str in dic[digits[i]]:
                    # 처음에 a,b,c
                    dfs(i + 1, str_temp + temp_str)

        dfs(0,"")
        return result

print(Solution().letterCombinations(digits))


temp_1 = "test"
temp_2 = temp_1

temp_1 = "fds"
print(temp_1)
print(temp_2)