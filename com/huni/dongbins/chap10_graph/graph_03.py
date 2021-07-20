# 도시 분할 계획

# 마을 N개의 집과 그 집들을 연결하는 M개의 길
# 길은 어느 방향이든 갈 수 있음
# 분할된 마을안에 집들이 서로 연결되도록 분할해야함
# 마을에는 집이 최소 한개는 존재


# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
#
# 8


def find_parent(parent, x):
    # 루트 노드가 아니라면 루트노드를 찾을떄까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0 #최소 신장 트리에서 가장 비용이 큰 간선

for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result - last)
