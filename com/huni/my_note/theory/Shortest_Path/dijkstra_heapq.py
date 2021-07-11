# 간단한 다익스트라 알고리즘

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의갯수, 간선의 갯수
n,m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단거리 테이블
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b에 가는 거리가 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 방문처리를 이렇게 한다.
        if distance[now] < dist:
            continue
        # 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


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


