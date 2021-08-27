# https://www.acmicpc.net/problem/14502

# 연구소

# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
#
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
#
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
#
# 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# 이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
#
# 2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

# 2 1 0 0 1 1 0
# 1 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 1 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# 바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
#
# 2 1 0 0 1 1 2
# 1 0 1 0 1 2 2
# 0 1 1 0 1 2 2
# 0 1 0 0 0 1 2
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.
#
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
#
# 27

# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2
#
# 9
#
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
#
# 3

# 이거 완전 생각이 안떠올랏음
# 완전탐색..

n,m = map(int, input().split())

# 초기 graph
data = [[] for _ in range(n)]

# 벽을 설치한 이후의 list
result_list = [[0] * m for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))
# print(data)
# print(result_list)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

# 바이러스 퍼트리는 함수
def virus_dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if result_list[nx][ny] == 0:
                result_list[nx][ny] = 2
                virus_dfs(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if result_list[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색으로 벽세우기하면서 안전영역계산
def dfs(count):
    global result

    # 울타리가 3개인 경우
    if count == 3:
        # 1. 결과 list에 맵핑
        for i in range(n):
            for j in range(m):
                result_list[i][j] = data[i][j]
        # 2. 바이러스를 전파 시킨다.
        for i in range(n):
            for j in range(m):
                if result_list[i][j] == 2:
                    virus_dfs(i,j)
        #3. 결과를 반영한다.
        result = max(result, get_score())
        return

    # 빈 공간에 울타리를 설치하는 경우 -> 백트래킹
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                count += 1
                data[i][j] = 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

