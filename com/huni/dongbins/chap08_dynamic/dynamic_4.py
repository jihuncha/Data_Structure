# 바닥 공사

n = int(input())

count_result = [0] * 1001
count_result[0] = 1
count_result[1] = 3


for i in range(2, n):
    count_result[i]  = count_result[i-1] + count_result[i-2] * 2

print(count_result[n-1])