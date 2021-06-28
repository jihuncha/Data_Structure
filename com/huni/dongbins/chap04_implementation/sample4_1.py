# 상하좌우

# N x N 의 공간
# 왼쪽위는 (1,1)


# 입력 예시
# 5
# R R R U D D

# 출력 예시
# 3 4

import sys

n = int(sys.stdin.readline())

moves_type = ["R","L","U","D"]

# rlud 순서로 구성한다.
dx = [0,0,-1,1]
dy = [1,-1,0,0]

data = list(map(str, sys.stdin.readline().split()))

# print(data)
position = (1,1)

for move in data:
    if move in moves_type:
        # position 설정
        nx = position[0] + dx[moves_type.index(move)]
        ny = position[1] + dy[moves_type.index(move)]

        # 범위 벗어나면 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        position = (nx, ny)
print(position)

#book coding_site_problem
# N 입력받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
#
# print(x, y)