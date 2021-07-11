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
import sys

INF = int(1e9)
input = sys.stdin.readline

# 노드와 간선의 갯수
n,m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for data in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)

visited = [False] * (n + 1)

distance = [INF] * (n + 1)
# print(distance)

def get_smallest_node():
    index = 0
    min_value = distance[index]
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            index = i
            min_value = distance[i]
    return index

def dijkstra(start):
    first_index = start
    distance[first_index] = 0
    visited[first_index] = True

    # 초기화
    for check in graph[start]:
        distance[check[0]] = check[1]
    for i in range(n - 1):
        temp_index = get_smallest_node()
        print(temp_index)
        visited[temp_index] = True
        for check_second in graph[temp_index]:
            result = distance[temp_index] + check_second[1]
            if distance[check_second[0]] > result:
                distance[check_second[0]] = result

    # print(distance)

dijkstra(start)

print(distance)


