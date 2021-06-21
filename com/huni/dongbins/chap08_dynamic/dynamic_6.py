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
    # print(array)

    # result_array = array
    # for i in range(n):
