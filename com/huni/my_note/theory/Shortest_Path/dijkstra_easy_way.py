# 간단한 다익스트라 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의갯수, 간선의 갯수
n,m = map(int, input().split())
# 시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문 여부 체스
visited = [False] * (n + 1)
# 최단거리 테이블
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b에 가는 거리가 c
    graph[a].append((b,c))

# 방문하지 않느 ㄴ노드 중에서, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 초기화 -> 방문처리
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        print(i)
        distance[i[0]] = i[1]

    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for j in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 가져온다.
        now = get_smallest_node()
        visited[now] = True

        for check in graph[now]:
            cost = check[1] + distance[now]
            if cost < distance[check[0]]:
                distance[check[0]] = cost

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


