# 못생긴 수

# 2,3,5 만을 소인수로 가지는 수

# 10
#
# 12
#
# 4
#
# 4


# 그냥풀이..
# n = int(input())
#
# data = [1]
#
# for i in range(2, 1001):
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
#         continue
#     data.append(i)
#
# print(data[n - 1])

# dp 사용
n = int(input())

dp = [0] * n
dp[0] = 1

num_2 = 2
num_3 = 3
num_5 = 5

idx_2 = 0
idx_3 = 0
idx_5 = 0

for i in range(1, n):
    dp[i] = min(num_2, num_3, num_5)

    if dp[i] == num_2:
        idx_2 += 1
        num_2 = dp[idx_2] * 2
    if dp[i] == num_3:
        idx_3 += 1
        num_3 = dp[idx_3] * 3
    if dp[i] == num_5:
        idx_5 += 1
        num_5 = dp[idx_5] * 5

print(dp)
print(dp[n-1])

