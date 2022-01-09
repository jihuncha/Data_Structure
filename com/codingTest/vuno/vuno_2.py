# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

# 4
# 3
# 4 1
# 7 9 2
# 2 7 9 6
# 1 9 5
# 7 3
# 9

# 50

# 5
# 6
# 1 2
# 6 7 4
# 9 4 1 7
# 6 7 5 9 4
# 4 4 3 2
# 1 2 3
# 6 1
# 7

# 48

n = int(input())

# 다이아몬드 데이터 생성
data = []
for i in range((n * 2) - 1):
    data.append(list(map(int, input().split())))

for i in range(1, (n * 2) - 1):
    # 다이아몬드 최대길이 위쪽부분까지는 분기처리하여 더해간다.
    if i < n:
        for j in range(len(data[i])):
            result = 0
            # 맨왼쪽의 경우
            if j == 0:
                up_right = data[i - 1][j]
                result = up_right
            # 맨 오른쪽의 경우
            elif j == len(data[i]) - 1:
                up_left = data[i - 1][j - 1]
                result = up_left
            # 그 외의 경우는 max값을 구해준다.
            else:
                up_right = data[i - 1][j]
                up_left = data[i - 1][j - 1]
                result = max(up_right, up_left)
            # 값을 갱신한다.
            data[i][j] = result + data[i][j]
    else:
        # 다이아몬드 최대길이 아래 부분은 위의 값중에 max 값을 구하여 더해서 갱신한다.
        for j in range(len(data[i])):
            data[i][j] = max(data[i-1][j], data[i-1][j+1]) + data[i][j]

print(data[(n * 2) - 2][0])
