# https://leetcode.com/problems/number-of-islands/

# 섬의 갯수
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
#
import collections

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# Output: 1
# Example 2:
#
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for x in range(len(grid))]
        print(visited)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        count = 0

        def iterative_dfs(x, y):
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                if grid[nx][ny] == "0" or visited[nx][ny]:
                    continue
                iterative_dfs(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not visited[i][j]:
                    iterative_dfs(i,j)
                    count+=1

        return count


print(Solution().numIslands(grid))

# 풀이
# from typing import List
#
#
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(i, j):
#             # 더 이상 땅이 아닌 경우 종료
#             if i < 0 or i >= len(grid) or \
#                     j < 0 or j >= len(grid[0]) or \
#                     grid[i][j] != '1':
#                 return
#
#             grid[i][j] = 0
#
#             # 동서남북 탐색
#             dfs(i + 1, j)
#             dfs(i - 1, j)
#             dfs(i, j + 1)
#             dfs(i, j - 1)
#
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     dfs(i, j)
#                     # 모든 육지 탐색 후 카운트 1 증가
#                     count += 1
#         return count