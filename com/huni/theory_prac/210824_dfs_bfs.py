# 재귀 dfs

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def recursive_dfs(start:int, visited=[]):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            recursive_dfs(i, visited)
    return visited

print(recursive_dfs(1))
# [1, 2, 5, 6, 7, 3, 4]

# stack
def iterative_dfs(start_v):
    discoverd = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discoverd:
            discoverd.append(v)
            for w in graph[v]:
                stack.append(w)

    return discoverd

print(iterative_dfs(1))
# [1, 4, 3, 5, 7, 6, 2]

def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if i not in discoverd:
                discoverd.append(i)
                queue.append(i)
    return discoverd

print(iterative_bfs(1))
# [1, 2, 3, 4, 5, 6, 7]


