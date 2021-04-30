# https://www.acmicpc.net/problem/2178

# 4 6
# 101111
# 101010
# 101011
# 111011
#
# 15
import collections
import sys

n,m = map(int, sys.stdin.readline().split())

print(n,m)

data_list = []
for i in range(n):
    data_list.append(list(map(int,input())))

visited = [[0] * m for _ in range(n)]

print(visited)

print(data_list)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

deque = collections.deque()
deque.append((0,0))
visited[0][0] = 1

count = 0
while deque:
    temp = deque.popleft()
    # print(deque)
    for i in range(4):
        next_x = temp[0] + dx[i]
        next_y = temp[1] + dy[i]

        if next_x < 0 or next_y < 0 or next_x > n - 1 or next_y > m - 1:
            continue

        if data_list[next_x][next_y] == 0:
            continue

        if visited[next_x][next_y] == 0 and data_list[next_x][next_y] == 1:
            visited[next_x][next_y] = visited[temp[0]][temp[1]] + 1
            deque.append((next_x, next_y))

        if next_x == n-1 and next_y == m-1:
            print(visited[next_x][next_y])
            break

    # bfs(next_x, next_y)

print(count)

# def bfs(x,y):
#     stack = []
#     stack.append((x,y))
#     visited[x][y] = True
#
#     while stack:
#         temp = stack.pop()


    # for i in range(4):
    #     next_x = x + dx[i]
    #     next_y = y + dy[i]
    #     if next_x < 0 or next_y < 0 or next_x > n - 1 or next_y > m - 1 or visited[next_x][next_y]:
    #         continue
    #     bfs(next_x, next_y)




# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# count = 0
#
# def dfs(x,y):
#     global count
#     print(x,y)
#     if x < 0 or x >= m - 1 or y < 0 or y >= n - 1:
#         return
#     if data_list[x][y] == 0:
#         return
#     if data_list[x][y] == 1:
#         count += 1
#     dfs(x + 1, y)
#     dfs(x - 1, y)
#     dfs(x, y + 1)
#     dfs(x, y - 1)
#
# dfs(0,0)
# print(count)




