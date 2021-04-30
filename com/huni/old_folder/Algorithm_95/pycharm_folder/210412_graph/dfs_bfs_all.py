#dfs - 알고리즘 인터뷰
#1. recursive
import collections
from typing import List
import collections

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def dfs_recursive(v, discoverd = []):
    discoverd.append(v)
    for w in graph[v]:
        if w not in discoverd:
            discoverd = dfs_recursive(w, discoverd)
    return discoverd

#2. for
def dfs_iterative(v) -> List:
    discoverd = []
    stack = [v]
    while stack:
        w = stack.pop()
        if w not in discoverd:
            discoverd.append(w)
            for i in graph[w]:
                stack.append(i)
    return discoverd

graph_a = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

result = []
# 이취코
def dfs(graph_a, v, visited):
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return result

# print(dfs(graph_a, 1, visited))

#bfs
def bfs_iterative(start_v):
    discoverd = [start_v]
    deque = collections.deque()
    deque.append(start_v)
    while deque:
        temp = deque.popleft()
        for i in graph[temp]:
            if i not in discoverd:
                deque.append(i)
                discoverd.append(i)
    return discoverd

print(bfs_iterative(1))

