graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

#재귀
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

print(recursive_dfs(1))

#반복문
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

#같은 dfs인데 값이 다르다
#1. 재귀의 경우 사전식 순서로 방문
#2. 스택으로 구현하다보니 가장 마지막에 삽입된 노드부터 반복

#bfs -> 재귀가안됨
def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discoverd:
                discoverd.append(w)
                queue.append(w)
    return discoverd

print(iterative_bfs(1))