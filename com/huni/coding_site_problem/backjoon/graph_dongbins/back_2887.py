# 행성 터널

# https://www.acmicpc.net/problem/2887

# 문제
# 때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.
#
# 행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
#
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다.
# 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다.
# 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다.
#
# 출력
# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

# input
# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19

# output
# 4

#####
# 최소 신장 트리로 풀어야할 것 같은데..
# 크루스칼

##### 풀이..
# 터널의 비용이 min(x좌표,y좌표,z좌표) 이므로
# 고려할 간선의 갯수를 1개 줄일수 있다 (5개이면 차이는 4개이므로)
# png파일 참고..뭔소리여


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드의 좌표값 받기
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

print(edges)

for edge in edges:
    cost,a,b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result += cost

print(result)