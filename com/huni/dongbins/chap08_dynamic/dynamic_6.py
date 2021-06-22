# 금광
test_case = int(input())

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
#
# 19
# 16


# 진짜 이런 생각을 떠올리는게 너무 어려운데..?

for i in range(test_case):
    n, m = map(int, input().split())
    data = list(map(int,input().split()))

    array = []
    temp = 0
    for i in range(n):
        array.append(data[temp:temp + m])
        temp += m
    print(array)

    for j in range(1, m):
        for i in range(n):
            # print(array[i][j])
            mid = array[i][j-1]
            if i - 1 < 0:
                top = 0
            else:
                top = array[i-1][j-1]

            if i + 1 > n - 1:
                bottom = 0
            else:
                bottom = array[i + 1][j - 1]

            array[i][j] = max(array[i][j] + top,array[i][j] + bottom,array[i][j] + mid)

    result = max([array[x][m-1] for x in range(n)])
    print(result)

