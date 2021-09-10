# 정확한 순위

# 이게뭔가싶었는데.. a->b 가는 경우 또는 b->a 가는 경우 무한대 아니면 비교가 가능하다는 뜻

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

# 1

import sys

INF = int(1e9)
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a,b = list(map(int, input().split()))
    graph[a][b] = 1

# print(graph)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)

result = 0
# count = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count +=1
    # 모두와 비교 가능한 경우
    if count == n:
        result += 1

print(result)