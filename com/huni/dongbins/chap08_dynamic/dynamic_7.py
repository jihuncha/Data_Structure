# 정수 삼각형

# 하나씩 선택해서 아래로 내려갈때 합이 최대가 되도록
# 대각선 왼쪽 및 오른쪽만 갈 수 있다.

# 입력
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 출력
# 30

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# print(array)

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

for i in range(1, n):
    for j in range(len(array[i])):
        if j == 0:
            left = 0
        else:
            left = array[i - 1][j - 1]
        if j == len(array[i])-1:
            right = 0
        else:
            right = array[i - 1][j]
        # print("test - ", i, j, left, right)

        array[i][j] = max(array[i][j] + left, array[i][j] + right)

            # array[i][j] = max(array[i][j] + array[i][j-1], array[i][j] + array[i][j+1])

print(max(array[n-1]))

