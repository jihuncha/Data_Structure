# 미로 탈출

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력
# 10

import sys

# n,m = map(int, sys.stdin.readline().split(" "))

n, m = map(int, input().split())

# print(n,m)

map_list = []
for i in range(n):
    map_list.append(list(map(int, input())))

print(map_list)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

result_list = []
def bfs(x, y, count):
    if x == n-1 and y == m-1:
        result_list.append(count)
        return
    # 범위에 벗어날 경우
    if x < 0 or y < 0 or x >= len(map_list) or y >= len(map_list[0]):
        return

    # 괴물 만나거나 이미 지나온 길인 경우
    if map_list[x][y] == 0 or map_list[x][y] > 1:
        print("out - ", map_list[x][y])
        return

    # 지나간 길의 경우 맵핑 해준다.
    if map_list[x][y] == 1:
        map_list[x][y] = count + 1
        count +=1

    # 상하좌우 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        bfs(nx,ny,count)

bfs(0,0,1)

print(min(result_list))
# print(map_list[n-1][m-1])


### 풀이
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))