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

# 0
# 2
# 3
# 1
# 2
# 4
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n,m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a,b,c = list(map(int, input().split()))
    graph[a].append((c,b))

distance = [INF] * (n + 1)

# print(graph)

def dijkstra(start:int):
    h = []
    distance[start] = 0

    heapq.heappush(h, (0, start))

    while h:
        dis, now = heapq.heappop(h)

        # 방문처리
        if distance[now] < dis:
            continue

        # 처리
        for i in graph[now]:
            cost = i[0] + dis
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(h, (cost, i[1]))

dijkstra(start)

print(distance)




