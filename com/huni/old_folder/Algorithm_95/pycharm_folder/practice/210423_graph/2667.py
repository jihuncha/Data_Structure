# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

import sys

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# print(graph)

visited = [[False] * (n+1) for _ in range(n+1)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dange = []
check_dange = 0
def dfs(x,y):
    global check_dange
    if x < 0 or y < 0 or x >= n or y >= n or visited[x][y] or graph[x][y] == 0:
        return
    visited[x][y] = True
    check_dange += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        dfs(nx,ny)

count = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y] and graph[x][y] == 1:
            check_dange = 0
            dfs(x,y)
            dange.append(check_dange)
            count+=1

print(count)
for i in sorted(dange):
    print(i)
# print(dange)


