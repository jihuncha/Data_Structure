# 5 5
# 0 0 0 0 0
# 0 0 1 0 0
# 0 1 1 1 1
# 0 0 0 1 0
# 0 0 0 0 0

# 12

# 6 8
# 0 0 0 0 0 0 1 1
# 0 0 1 0 0 0 0 1
# 0 1 1 1 1 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 1 1 1 1 1 1 1

# 23

# 3 3
# 0 0 1
# 0 1 0
# 1 0 0

# 3

n, m = map(int, input().split())

# graph
data = [[] for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))

# 영역의 합을 담을 result
result = 0

# dfs를 통한 반복 (x좌표, y좌표, 방문한 x_list, 방문한 y_list)
def dfs(x:int, y:int, x_list:list, y_list:list):
    # 주어진 범위를 벗어나는 경우 또는 2인 경우는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m or data[x][y] == 2:
        return [x_list,y_list]
    if data[x][y] == 1:
        # 방문 처리로 2를 대입한다.
        data[x][y] = 2
        # 임시 list에 해당 값을 추가한다.
        x_list.append(x)
        y_list.append(y)
        # 상하좌우로 반복을한다.
        dfs(x - 1, y,x_list, y_list)
        dfs(x, y - 1,x_list, y_list)
        dfs(x + 1, y,x_list, y_list)
        dfs(x, y + 1,x_list, y_list)
    return [x_list, y_list]

for i in range(n):
    for j in range(m):
        # x좌표 list 및 y좌표 list
        temp_x, temp_y = dfs(i,j,[],[])
        # list가 존재하는 경우
        if temp_x:
            # 한칸인 경우는 넓이 1로 처리한다
            if len(temp_x) == 1:
                result += 1
            # 한칸이 아닌 경우는 max길이 및 min 길이를 구해서 영역값을 계산하여 result에 담는다
            else:
                min_x = min(temp_x)
                max_x = max(temp_x)
                min_y = min(temp_y)
                max_y = max(temp_y)
                result += (max_x - min_x + 1) * (max_y - min_y + 1)

print(result)

