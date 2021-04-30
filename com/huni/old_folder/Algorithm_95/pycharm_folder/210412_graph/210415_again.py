from typing import List
import collections

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def dfs_recursive(v, discoverd = []):
    discoverd.append(v)
    for i in graph[v]:
        if i not in discoverd:
            dfs_recursive(i,discoverd)
    return discoverd

# print(dfs_recursive(1))

def dfs_iterative(v):
    discoverd = []
    stack = [v]

    while stack:
        temp = stack.pop()
        if temp not in discoverd:
            discoverd.append(temp)
        for i in graph[temp]:
            if i not in discoverd:
                stack.append(i)
    return discoverd

# print(dfs_iterative(1))

def bfs_iterative(v):
    discoverd = [v]
    queue = collections.deque()
    queue.append(v)

    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if i not in discoverd:
                discoverd.append(i)
                queue.append(i)
    return discoverd
# print(bfs_iterative(1))

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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        # for i in range(len(visited[0])):
        #     for j in range(len(visited)):
        #         print(i,j)

        # print(visited[4][0])
        nx = [-1,1,0,0]
        ny = [0,0,-1,1]
        def dfs(x,y):
            # print(x,y)
            if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) -1 or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for i in range(4):
                dfs(x + nx[i], y + ny[i])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)

                    count +=1

        return count
# print(Solution().numIslands(grid))

########################################################################################################################
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

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        result = []
        temp_str = ""

        def dfs(index, input_data):
            # print(index, input_data)
            if len(digits) == len(input_data):
                result.append(input_data)
                return
            for i in range(index, len(digits)):
                print(i)
                for k in dic[digits[i]]:
                    # print(k)
                    dfs(i + 1, input_data + k)

        dfs(0,"")
        print(result)

print(Solution().letterCombinations(digits))