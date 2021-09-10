# 다익스트라

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
#
# 0
# 2
# 3
# 1
# 2
# 4

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
#
# n,m = map(int, input().split())
#
# # print(n,m)
#
# start_index = int(input())
#
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     x,y,length = list(map(int, input().split()))
#     graph[x].append((y, length))
#
# # print(graph)
# distance = [INF] * (n+1)
#
# def dijkstra(start:int):
#     distance[start] = 0
#     q = [(0, start)]
#
#     while q:
#         dist, index = heapq.heappop(q)
#
#         if distance[index] < dist:
#             continue
#
#         for check in graph[index]:
#             cost = dist + check[1]
#             if cost < distance[check[0]]:
#                 distance[check[0]] = cost
#                 heapq.heappush(q, (cost, check[0]))
#
# dijkstra(start_index)
#
# print(distance)


# 플로이드 워셜

# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

n = int(input())

m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# print(graph)

for i in range(1, n+1):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a,b,c = list(map(int, input().split()))
    graph[a][b] = c

print(graph)

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

print(graph)

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF")
        else:
            print(graph[i][j], end=' ')
    print()