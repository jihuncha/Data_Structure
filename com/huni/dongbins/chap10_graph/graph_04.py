# 커리큘럼

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1


# def find_parent(parent, a):
#     if parent[a] != a:
#         parent[a] = find_parent(parent, parent[a])
#     return parent[a]
#
# def union_parent(parent, a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

from collections import deque
import copy

v = int(input())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

time = [0] * (v + 1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫번쨰수는 시간 정보
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    # result에 단순 대입연산을 하면 값이 변경되기떄문..
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()