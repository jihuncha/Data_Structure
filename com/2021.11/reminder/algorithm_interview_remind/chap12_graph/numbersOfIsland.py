# https://leetcode.com/problems/number-of-islands/
from typing import List


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# Output: 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        count = 0

        # print(grid)
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        # print(visited)

        def dfs(x,y):
            visited[x][y] = True

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or visited[nx][ny] or grid[nx][ny] == '0':
                    continue

                dfs(nx,ny)

        for start_x in range(len(grid)):
            for start_y in range(len(grid[0])):
                if not visited[start_x][start_y] and grid[start_x][start_y] == '1':
                    dfs(start_x, start_y)

                    count += 1
        return count

print(Solution().numIslands(grid))