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
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)

def dijkstra(start:int):
    heap = []
    distance[start] = 0

    heapq.heappush(heap, (0, start))

    while heap:
        dist, index = heapq.heappop(heap)

        # 방문처리 체크
        if distance[index] < dist:
            continue

        for i in graph[index]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijkstra(start)

print(distance)