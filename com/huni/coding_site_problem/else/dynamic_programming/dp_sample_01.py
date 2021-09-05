# 금광

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
import copy

test_case = int(input())

for i in range(test_case):
    n,m = map(int, input().split())
    temp = list(map(int, input().split()))

    result = []
    for i in range(n):
        result.append(temp[m*i: (m*i) + m])

    # print(result)

    # dp = copy.deepcopy(result)
    # for j in range(n):
    #     dp[j] = result[j][0]
    # print(dp)

    # dp = []
    # index = 0
    # for i in range(n):
    #     dp.append(result)

    for j in range(1,m):
        for i in range(n):
            left = result[i-1][j-1] if i-1 >= 0 else 0
            mid = result[i][j-1]
            right = result[i+1][j-1] if i+1 < n else 0
            # print(left,mid,right)
            result[i][j] = result[i][j] + max(left,mid,right)

    # print(result)

    result_sum = 0
    for i in range(n):
        result_sum = max(result_sum, result[i][m-1])
    print(result_sum)


# for i in range(n):
