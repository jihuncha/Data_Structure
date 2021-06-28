# https://www.acmicpc.net/problem/2110

# 공유기 설치

# 문제
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
#
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에,
#
# 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
#
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
#
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
#
# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
#
# 예제 입력
# 5 3
# 1
# 2
# 8
# 4
# 9
#
# 예제 출력
# 3
#
# 힌트
# 공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.

# 7 4
# 1
# 2
# 4
# 9
# 11
# 22
# 33

# 2 2
# 1
# 99

n,c = map(int,input().split())

data = [int(input()) for _ in range(n)]

# print(data)

data.sort()

# gap 차이를 바탕으로
left = data[1] - data[0]
right = data[n-1] - data[0]
result = 0

while left <= right:
    mid = (left + right) // 2
    # 처음위치 value 및 count 설정 (1)
    value = data[0]
    count = 1

    for i in range(1,len(data)):
        if data[i] >= value + mid:
            count += 1
            value = data[i]

    # for check in data[1:]:
    #     if check >= mid + value:
    #         value = check
    #         count += 1
    # 설치한것이 조건에 충전한 경우
    # gap 을 늘려준다. 결과를 가지고 있는다.
    if count >= c:
        left = mid + 1
        result = mid
    # 부족한 경우
    # gap 을 좁혀준다.
    else:
        right = mid - 1

print(result)

# left = 0
# right = len(data) - 1

# count = c - 2
#
# index_list = [data[left], data[right]]
#
# def binary_search(count, left, right):
#     mid = (left+right) // 2
#     index_list.append(data[mid])
#
#     count -= 1
#     if count == 0:
#         return
#     else:
#         binary_search(count, left, mid - 1)
#         binary_search(count, mid + 1, right)
#
#
# # while left <= right:
# #     mid = (left+right) // 2
# #     index_list.append(data[mid])
# #
# #     count -= 1
# #     # break
# #     if count == 0:
# #         break
# #     else:
#
# if n > 2:
#     binary_search(count, left, right)
#     index_list.sort()
#
#     # print(index_list)
#
#     result_list = []
#     for k in range(len(index_list) - 1):
#         result_list.append(index_list[k + 1] - index_list[k])
#
#     print(min(result_list))
# else:
#     print(data[1]-data[0])


n, c = map(int, input().split())

house = []
for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 좌표값의 최소값
start = 1
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start + end) // 2  # 해당 gap
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid:  # gap 이상
            count += 1
            old = house[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)



