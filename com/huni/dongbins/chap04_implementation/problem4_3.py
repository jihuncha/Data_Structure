# 왕실의 나이트

# 8 * 8 에서 좌표값 부여해줬을때 이동할수 있는 경우의수 구하는 문제

# input
# a1

# output
# 2

import sys

position = str(input())
# print(position[0])

# 경우의 수 설정 -> 8가지
move_types = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

# ord 사용
# print(ord('a'))

count = 0

for move in move_types:
    nx = int(ord(position[0])) + move[0]
    ny = int(position[1]) + move[1]

    if nx < ord('a') or ny < 1 or nx > ord('h') or ny > 8:
        continue

    # print(chr(nx), ny)
    count += 1

print(count)

# book answer

# 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)