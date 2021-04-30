# https://www.acmicpc.net/problem/1260

#1.
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
#
# 1 2 4 3
# 1 2 3 4

#2.
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

#3.
# 1000 1 1000
#999 1000

# 6 5 6
# 5 4
# 4 6
# 2 3
# 3 1
# 1 6
# ----
# 6 1 3 2 4 5
# 6 1 4 3 5 2
import collections
import sys

n,m,v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

# print(graph)

visited = [False for _ in range(n+1)]

# print(visited)


dfs_result = []
bfs_result = []

def dfs(start:int):
    # 방문 처리
    visited[start] = True
    dfs_result.append(start)
    for idx,i in enumerate(graph[start]):
        # print(visited[idx])
        if i == 1 and not visited[idx]:
            dfs(idx)

temp_deque = collections.deque()
def bfs(start:int):
    bfs_result.append(start)
    temp_deque.append(start)
    visited[start] = True
    while temp_deque:
        temp = temp_deque.popleft()
        for idx,i in enumerate(graph[temp]):
            if i == 1 and not visited[idx]:
                visited[idx] = True
                temp_deque.append(idx)
                bfs_result.append(idx)

dfs(v)
visited = [False for _ in range(n+1)]
bfs(v)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
