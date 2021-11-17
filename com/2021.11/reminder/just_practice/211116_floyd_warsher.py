# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

n = int(input())
m = int(input())
INF = 1e9

graph = [[INF] * (n+1) for _ in range(n+1)]

# print(graph)

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# print(graph)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

print(graph)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j], end=' ')
    print("")