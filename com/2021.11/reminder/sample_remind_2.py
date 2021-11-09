# 인접행렬

INF = int(1e9)

graph = [
    [0,7,5],
    [7,0,INF],
    [5, INF, 0]
]

print(graph)

graph = [[] for _ in range(3)]

#노드와 거리
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장
graph[1].append((0,7))

#노드 2에 연결된 노드 정보 저장
graph[2].append((0,5))

print(graph)

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

print(graph)

visited = [False for _ in range(8)]
print(visited)

result = []
def dfs(start:int):
    result.append(start)
    visited[start] = True
    print(visited)
    for i in graph[start]:
        if not visited[i] and i not in result:
            dfs(i)

dfs(1)
print(result)
