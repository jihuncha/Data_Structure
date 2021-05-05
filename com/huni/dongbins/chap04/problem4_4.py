# 게임 개발

# input
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# output
# 3

import sys

# 이거 bfs로도 풀수있을거같은데 ????

# map
n, m = map(int, sys.stdin.readline().split())
# 좌표 및 방향
x, y, d = map(int, sys.stdin.readline().split())
# 데이터
data = []
# 방향 북 서 남 동
d_move = [0, 3, 2, 1]
# 움직일 수 있는 방향 (북 서 남 동)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 방문 여부 체크
visited = [[False] * m for _ in range(n)]

# print(visited)

# map 만들기
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

# print(data)

# 초기 값 설정 (차음위치 방문 처리)
count = 1
visited[x][y] = True

# 방향 정의
# direction = d_move.index(d)

# 이게 아마 bfs??느낌
def move(x,y,d):
    global count
    for i in range(4):
        if d == 3:
            d = 0
        else:
            d += 1

        # 이동할 위치
        nx = x + dx[d]
        ny = y + dy[d]
        # print(nx, ny)

        # 해당 위치가 방문한 적있거나 바다면 continue
        if visited[nx][ny] or data[nx][ny] == 1:
            continue

        count += 1
        visited[nx][ny] = True
        # 해당 좌표에서 재실행
        move(nx, ny, d)

move(x,y,d)

print(count)



#book_answer
# # N, M을 공백을 기준으로 구분하여 입력받기
# n, m = map(int, input().split())
#
# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0] * m for _ in range(n)]
# # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
# x, y, direction = map(int, input().split())
# d[x][y] = 1 # 현재 좌표 방문 처리
#
# # 전체 맵 정보를 입력받기
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# # 북, 동, 남, 서 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# # 왼쪽으로 회전
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
#
# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     # 왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있는 경우
#         else:
#             break
#         turn_time = 0
#
# # 정답 출력
# print(count)












