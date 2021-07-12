# 전보

# 3 2 1
# 1 2 4
# 1 3 2

# 2 4

import sys
import heapq

# INF = int(1e9)
# input = sys.stdin.readline
#
# n,m,c = map(int,input().split())
#
# data = [[INF] * (n + 1) for _ in range(n+1)]
#
# for _ in range(m):
#     a,b,c, = map(int,input().split())
#     data[a][b] = c
#
# print(data)
#
# for k in range(1, n+1):
#     for b in range(1, n+1):
#         data[c][b] = min(data[c][b], data[c][k] + data[k][b])
#
# print(data)
#
# count = 0
# max_value = 0
# for i in range(1, n+1):
#     for j in data[i]:
#         if j != INF:
#             count += 1
#             max_value = max(max_value, j)
#
# print(count, max_value)


######## 다익스트라로 풀어야함!! n,m 범위가 너무 넓다!!

INF = int(1e9)
input = sys.stdin.readline

n,m,start = map(int,input().split())

# data = [[INF] * (n + 1) for _ in range(n+1)]

data = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a,b,c = map(int,input().split())
    data[a].append((b,c))

print(data)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue

        for check in data[now]:
            cost = check[1] + dist
            if cost < distance[check[0]]:
                distance[check[0]] = cost
                heapq.heappush(q, (cost, check[0]))

dijkstra(start)

print(distance)

count = 0
max_dist = 0

for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)

# 시작 노드 제외 필요
print(count - 1, max_dist)
