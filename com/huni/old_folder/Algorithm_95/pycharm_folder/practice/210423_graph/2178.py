# 4 6
# 101111
# 101010
# 101011
# 111011
import collections
import sys

n,m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = collections.deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for temp in range(4):
            nx = x + dx[temp]
            ny = y + dy[temp]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))



