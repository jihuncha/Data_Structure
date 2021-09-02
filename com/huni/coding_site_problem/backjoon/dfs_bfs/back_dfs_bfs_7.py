# https://www.acmicpc.net/problem/16234

# 인구 이동

# 문제
# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며,
# r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.
#
# 오늘부터 인구 이동이 시작되는 날이다.
#
# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
#
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
#
# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
#
# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.
#
# 출력
# 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

# 2 20 50
# 50 30
# 20 40

# 1

# 2 40 50
# 50 30
# 20 40

# 0

# 2 20 50
# 50 30
# 30 40

# 1

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# 2

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10
#
# 3

# n,l,r = map(int, input().split())
#
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# # print(data)
#
# check_connect = [[0] * n for _ in range(n)]
# # print(check_connect)
#
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# def connecting():
#     for a in range(n):
#         for b in range(n):
#             for i in range(4):
#                 nx = a + dx[i]
#                 ny = b + dy[i]
#                 if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
#                     continue
#                 num = abs(data[nx][ny] - data[a][b])
#                 if num >= l and num <= r:
#                     if check_connect[a][b] == 0:
#                         check_connect[a][b] = int(str(a + 1) + str(b + 1))
#                     check_connect[nx][ny] = check_connect[a][b]
#
# def make_new_list():
#     sum = 0
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if check_connect[i][j] != 0:
#                 sum += data[i][j]
#                 count += 1
#     print(sum//count)
#
#     result_num = sum//count
#
#     for i in range(n):
#         for j in range(n):
#             if check_connect[i][j] != 0:
#                 data[i][j] = result_num
#
# def check_end() -> bool:
#     for i in range(n):
#         for j in range(n):
#             if check_connect[i][j] != 0:
#                 return False
#     return True
#
# result = 0
#
# while True:
#     # 연결 처리
#     connecting()
#     print(check_connect)
#
#     # 더 되는 경우 없는 경우는 빠져 나간다
#     if check_end():
#         break
#     # 새 데이터 list를 만든다
#     make_new_list()
#
#     # 초기화
#     check_connect = [[0] * n for _ in range(n)]
#     # 결과값 추가
#     result += 1
#
#
# # connecting()
# # print(check_connect)
# # print(make_new_list())
#
# print(result)

# check_roof = False
#
# while check_roof:
#     connecting()

# def connect(temp:tuple):
#     my_temp_num = int(str(temp[0] + 1) + str(temp[1] + 1))
#     print(my_temp_num)
#     # print(my_temp_num)
#     check_connect[temp[0]][temp[1]] = my_temp_num
#     for i in range(4):
#         nx = temp[0] + dx[i]
#         ny = temp[1] + dy[i]
#         # print(nx,ny)
#         if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1 \
#                 or check_connect[nx][ny] != 0:
#             continue
#         num = abs(data[nx][ny] - data[temp[0]][temp[1]])
#         if num >= l and num <= r:
#             check_connect[nx][ny] = my_temp_num
#             connect((nx,ny))


# connect((0,0))
# print(check_connect)

######################################################################################################

# 풀이
# 모든 나라의 위치에서 DFS/BFS 수행 -> 인접한 나라의 인구 확인하여 처리

from collections import deque
# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)