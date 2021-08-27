# https://www.acmicpc.net/problem/18405

# 경쟁적 전염

# NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.
#
# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
#
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
#
# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
#
# 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.
#
# 예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.

# [back_dfs_bfs_3_1]

# 1초가 지난 후에 시험관의 상태는 다음과 같다.
#
# [back_dfs_bfs_3_2]
#
# 2초가 지난 후에 시험관의 상태는 다음과 같다.
#
# [back_dfs_bfs_3_3]
#
# 결과적으로 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류는 3번 바이러스다. 따라서 3을 출력하면 정답이다.

# 입력
# 첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000)
# 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다.
# 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다.
# N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)
#
# 출력
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2
#
# 3

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2

# 0

# import copy
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
temp_hold = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            temp_hold.append((graph[i][j],0, i,j))

s,x,y = map(int, input().split())

temp_hold.sort()
queue = deque(temp_hold)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    data = queue.popleft()
    # print(data)
    if data[1] == s:
        continue

    for i in range(4):
        nx = data[2] + dx[i]
        ny = data[3] + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = data[0]
                queue.append((data[0], data[1] + 1, nx, ny))

print(graph[x-1][y-1])












# temp_graph = copy.deepcopy(graph)
# print(temp_graph)
#
# for time in range(s):
#     graph = copy.deepcopy(temp_graph)
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] != 0:
#                 for move in range(4):
#                     nx = i + dx[move]
#                     ny = j + dy[move]
#
#                     if nx >= 0 and nx < n and ny >= 0 and ny < m:
#                         if temp_graph[nx][ny] == 0:
#                             temp_graph[nx][ny] = graph[i][j]
#
# print(temp_graph[x-1][y-1])