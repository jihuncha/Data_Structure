# 뱀

#

# 문제
#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데,
#
# 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
#
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
#
# 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
#
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
#
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
#
# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
#
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
#
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
#
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며.
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.
#
# 출력
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

# 예제 입력 1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
#
# 예제 출력 1
# 9
#
# 예제 입력 2
# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L
#
# 예제 출력 2
# 21
#
# 예제 입력 3
# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L
#
# 예제 출력 3
# 13
import collections
import sys

n = int(sys.stdin.readline())

# 보드 생성
my_board = [[0] * n for _ in range(n)]

# 사과 맵핑
apple_count = int(sys.stdin.readline())
for i in range(apple_count):
    a,b = list(map(int, sys.stdin.readline().split()))
    my_board[a-1][b-1] = 2

# apple은 2로 설정하여 위치 체크
# print(my_board)

# 좌표 변동 시간
change_count = int(sys.stdin.readline())
change_data = {}
for i in range(change_count):
    a,b = list(map(str, sys.stdin.readline().split()))
    change_data[int(a)] = b

# 체크
# print(change_data)

# 상하좌우 이동
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 뱀의 길이
# snake_len = 1

second = 0
my_board[0][0] = 1

def move_index(x,y,index):
    return [x + dx[index], y + dy[index]]

deque_list = collections.deque()

first_index = 0

current_a, current_b = 0,0

while True:
    next_a, next_b = move_index(current_a, current_b, first_index)
    # print(next_a, next_b)
    # print("second - ", second)
    # 머리가 좌표값을 벗어난 경우 / 몸통 만난 경우는 그대로 break
    if next_a > n - 1 or next_b > n - 1 or next_a < 0 or next_b < 0 or my_board[next_a][next_b] == 1:
        break

    #사과가 있는 경우는 길이를 증가
    if my_board[next_a][next_b] == 2:
        # snake_len += 1
        # 꼬리 부분 append
        deque_list.append((current_a,current_b))
        # print(deque_list)
        # 현재 좌표값 갱신
        current_a, current_b = next_a, next_b
        my_board[current_a][current_b] = 1

        # 사과를 먹어도 초는 더해줘야되지?
        second += 1

        # print(my_board)
        # 다음 좌표 변경
        if second in change_data:
            if change_data[second] == 'D':
                first_index += 1
                if first_index > 3:
                    first_index = 0
            if change_data[second] == 'L':
                first_index -= 1
                if first_index < 0:
                    first_index = 3
        continue

    # 사과가 없는 경우는 뒷부분을 땅긴다.
    # print("no apple")
    if deque_list:
        temp_a, temp_b = deque_list.popleft()
        # print("222", my_board[temp_a][temp_b])
        my_board[temp_a][temp_b] = 0
        deque_list.append((current_a, current_b))
    else:
        my_board[current_a][current_b] = 0

    my_board[next_a][next_b] = 1
    # print(my_board)
    # 증가 시킨다.
    current_a, current_b = next_a, next_b
    second += 1

    if second in change_data:
        if change_data[second] == 'D':
            first_index += 1
            if first_index > 3:
                first_index = 0
        if change_data[second] == 'L':
            first_index -= 1
            if first_index < 0:
                first_index = 3

print(second + 1)





