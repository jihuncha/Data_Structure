graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def recursive_dfs(v, discoverd=[]):
    discoverd.append(v)
    for w in graph[v]:
        if w not in discoverd:
            recursive_dfs(w, discoverd)
    return discoverd


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


#[1, 2, 5, 6, 7, 3, 4]
print(recursive_dfs(1))

# [1, 4, 3, 5, 7, 6, 2]
print(iterative_dfs(1))


