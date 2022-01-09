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

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())

# print(n,m)

start_index = int(input())

graph = [[] for _ in range(n + 1)]

# print(graph)

# 동일함
# visited = [False for _ in range(n+1)]
visited = [False] * (n + 1)

# print(visited)

distance = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,c = list(map(int, input().split()))
    graph[a].append((b,c))

print(graph)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijstra(start:int):
    # 방문처리
    distance[start] = 0
    visited[start] = True

    # 맵핑 
    for i in graph[start]:
        distance[i[0]] = i[1]
        
    # 잔여 위치에 대해서
    for j in range(n-1):
        # 거리 가장 짧은놈 가져온다
        index = get_smallest_node()
        # 해당 위치 방문처리
        visited[index] = True
        
        # 방문한 인접노드 체크
        for k in graph[index]:
            if distance[index] + k[1] < distance[k[0]]:
                distance[k[0]] = distance[index] + k[1]


dijstra(start_index)

print(distance)

                
