# 개미 전사

# input
# 4
# 1 3 1 5
#
# output
# 8

n = int(input())

data = list(map(int, input().split()))

# print(data)

sum_list = [0] * 101
sum_list[0] = data[0]
sum_list[1] = max(data[1], data[0])

# print(sum_list)

# n+2 번쨰 최대값은 n+1 까지의 합 또는 n 번쨰 합 + 현재 값의 max로 표현

for i in range(2, n):
    sum_list[i] = max(sum_list[i-1], sum_list[i-2] + data[i])

print(sum_list[n - 1])
