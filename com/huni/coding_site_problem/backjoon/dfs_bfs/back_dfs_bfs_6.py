# https://www.acmicpc.net/problem/18428

# 감시 피하기

# NxN 크기의 복도가 있다. 복도는 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다.
# 현재 몇 명의 학생들은 수업시간에 몰래 복도로 빠져나왔는데, 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.
#
# 각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 단, 복도에 장애물이 위치한 경우,
# 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다. 또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.
#
# 다음과 같이 3x3 크기의 복도의 정보가 주어진 상황을 확인해보자.
# 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다.
# 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S, 장애물이 존재하는 칸은 O로 표시하였다.
# 아래 그림과 같이 (3,1)의 위치에는 선생님이 존재하며 (1,1), (2,1), (3,3)의 위치에는 학생이 존재한다. 그리고 (1,2), (2,2), (3,2)의 위치에는 장애물이 존재한다.

# [temp_1]

# 이 때 (3,3)의 위치에 존재하는 학생은 장애물 뒤편에 숨어 있기 때문에 감시를 피할 수 있다. 하지만 (1,1)과 (2,1)의 위치에 존재하는 학생은 선생님에게 들키게 된다.
#
# 학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라,
# 정확히 3개의 장애물을 설치해야 한다. 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산하고자 한다.
# NxN 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하시오.
#
# 예를 들어 N=5일 때, 다음과 같이 선생님 및 학생의 위치 정보가 주어졌다고 가정하자.

# [temp_2]

# 이 때 다음과 같이 3개의 장애물을 설치하면, 모든 학생들을 선생님의 감시로부터 피하도록 만들 수 있다.

# [temp_3]

# 입력
# 첫째 줄에 자연수 N이 주어진다. (3 ≤ N ≤ 6) 둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다.
# 각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다. 해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
#
# 단, 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며 항상 빈 칸의 개수는 3개 이상으로 주어진다.
#
# 출력
# 첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다.
# 모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력한다.


# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# YES

# 4
# S S S T
# X X X X
# X X X X
# T T T X

# NO
import copy

# 포기

# n = int(input())
#
# data = []
# for i in range(n):
#     data.append(list(map(str, input().split())))
#
# # 0 통로 / 1 학생 / 2 선생
# for i in range(n):
#     for j in range(n):
#         if data[i][j] == 'X':
#             data[i][j] = 0
#         elif data[i][j] == 'S':
#             data[i][j] = 1
#         else:
#             data[i][j] = 2
# print(data)
#
# temp_result = data[:]
# result_bool = False
#
# # 3개 넣음
# def make_bridge(make_list:list, count:int, check_list:list):
#     if result_bool:
#         return
#
#     if count == 3:
#         isCorrect(make_list,check_list)
#         return
#
#     for i in range(n):
#         for j in range(n):
#             if make_list[i][j] == 0:
#                 make_list[i][j] = 3
#                 count += 1
#                 check_list.append((i,j))
#                 make_bridge(make_list, count, check_list)
#                 make_list[i][j] = 0
#                 count -= 1
#                 check_list.remove((i,j))
#
#
# def isCorrect(all_list:list, check_list:list):
#     result_list = []
#     for i in check_list:
#         result_list.append(search(all_list, i))
#     print(result_list)
#
#
#
# def search(my_list:list, check:tuple):
#     left = my_list[check[0]][:check[1]]
#     if left:
#         left.reverse()
#     right = my_list[check[0]][check[1] + 1:]
#     top_bottom = [my_list[x][check[1]] for x in range(n)]
#     bottom = top_bottom[check[0] + 1:]
#     top = top_bottom[:check[0]]
#     if top:
#         top.reverse()
#
#     # print(top, right,bottom, left)
#
#     check = False
#
#     for a in top:
#         if a == 1:
#             check = True
#             return check
#         if a == 3:
#             break
#
#     for b in left:
#         if b == 1:
#             check = True
#             return check
#         if b == 3:
#             break
#
#     for c in bottom:
#         if c == 1:
#             check = True
#             return check
#         if c == 3:
#             break
#
#     for d in left:
#         if d == 1:
#             check = True
#             return check
#         if d == 3:
#             break
#
#     return check
#
# print(make_bridge(temp_result, 0, []))
#
# print(result_bool)


######################################################################################################

# 풀이
# 최대 경우의 수 36C3 -> 1000이하의 수 -> 완전 탐색해라

from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보 (N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행 (학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물들을 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')