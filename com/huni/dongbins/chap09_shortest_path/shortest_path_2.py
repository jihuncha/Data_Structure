# 미래 도시

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
#
# 3
#
# 4 2
# 1 3
# 2 4
# 3 4
#
# -1

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

data = [[INF] * (n + 1) for _ in range(n+1)]

print(data)

# 같은 경올는 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            data[i][j] = 0

# 데이터 입력
for i in range(m):
    a,b = map(int, input().split())
    data[a][b] = data[b][a] = 1

print(data)

x, k = map(int, input().split())

# count = 0

for temp_1 in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            data[a][b] = min(data[a][b], data[a][temp_1] + data[temp_1][b])

print(data)

result = data[1][k] + data[k][x]
# print(result)

if result >= INF:
    print("-1")
else:
    print(result)
