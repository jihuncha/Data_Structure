# 큰 수의 법칙

# input
# 5 8 3
# 2 4 5 4 6

# output
# 46

# My Answer
import sys

n, m, k = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort(reverse=True)

print(num_list)

count = 0
result = 0
for i in range(m):
    if count >= k and len(num_list) > 1:
        count = 0
        result += num_list[1]
    else:
        count+=1
        result += num_list[0]

print(result)

# Book Answer

# # N, M, K를 공백을 기준으로 구분하여 입력 받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백을 기준으로 구분하여 입력 받기
# data = list(map(int, input().split()))
#
# data.sort() # 입력 받은 수들 정렬하기
# first = data[n - 1] # 가장 큰 수
# second = data[n - 2] # 두 번째로 큰 수
#
# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k + 1)) * k
# count += m % (k + 1)
#
# result = 0
# result += (count) * first # 가장 큰 수 더하기
# result += (m - count) * second # 두 번째로 큰 수 더하기
#
# print(result) # 최종 답안 출력