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

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())

start_index = int(input())

data = [[] for _ in range(n + 1)]

for make_data in range(m):
    a,b,c = map(int, input().split())
    data[a].append((b,c))

print(data)

distance = [INF] * (n + 1)

def dijkstra(start:int):
    q = []
    distance[start] = 0
    # 순서주의!! -> 거리로 최소 힙순서대로 가야한다.
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in data[now]:
            cost = i[1] + distance[now]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start_index)

print(distance)




