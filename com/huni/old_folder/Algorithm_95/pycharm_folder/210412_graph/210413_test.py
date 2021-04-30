from typing import List

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Output: 1
#
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            print(x,y)
            if grid[x][y] != '1' or x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) -1 :
            #     print("what? : ",x,y)
            #     return
            # if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
                return
            grid[x][y] = 0

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        count = 0
        # x = y = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)

                    count +=1
        return count
        # dfs(x,y)


print(Solution().numIslands(grid))