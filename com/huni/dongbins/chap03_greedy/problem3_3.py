# 숫자 카드 게임

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2

# 2 4
# 7 3 1 8
# 3 3 3 4
#
# 3


import sys


n,m = map(int, sys.stdin.readline().split())

# 내 풀이
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

print(data)

result = 0
for i in data:
    temp = min(i)
    result = max(result, temp)

print(result)

# 책

# # N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())
#
# result = 0
# # 한 줄씩 입력 받아 확인하기
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
#     # '가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
#
# print(result) # 최종 답안 출력