# https://www.acmicpc.net/problem/1052

# 문제
# 지민이는 N개의 물병을 가지고 있다.
# 각 물병에는 물을 무한대로 부을 수 있다.
# 처음에 모든 물병에는 물이 1리터씩 들어있다.
# 지민이는 이 물병을 또 다른 장소로 옮기려고 한다.
# 지민이는 한 번에 K개의 물병을 옮길 수 있다.
# 하지만, 지민이는 물을 낭비하기는 싫고, 이동을 한 번보다 많이 하기는 싫다.
# 따라서, 지민이는 물병의 물을 적절히 재분배해서, K개를 넘지 않는 비어있지 않은 물병을 만들려고 한다.
#
# 물은 다음과 같이 재분배 한다.
#
# 먼저 같은 양의 물이 들어있는 물병 두 개를 고른다.
# 그 다음에 한 개의 물병에 다른 한 쪽에 있는 물을 모두 붓는다.
# 이 방법을 필요한 만큼 계속 한다.
#
# 이런 제약 때문에, N개로 K개를 넘지않는 비어있지 않은 물병을 만드는 것이 불가능할 수도 있다.
# 다행히도, 새로운 물병을 살 수 있다. 상점에서 사는 물병은 물이 1리터 들어있다.
#
# 예를 들어, N=3이고, K=1일 때를 보면, 물병 3개로 1개를 만드는 것이 불가능하다.
# 한 병을 또다른 병에 부으면, 2리터가 들어있는 물병 하나와, 1리터가 들어있는 물병 하나가 남는다.
# 만약 상점에서 한 개의 물병을 산다면, 2리터가 들어있는 물병 두 개를 만들 수 있고, 마지막으로 4리터가 들어있는 물병 한 개를 만들 수 있다.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. N은 107보다 작거나 같은 자연수이고, K는 1,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 상점에서 사야하는 물병의 최솟값을 출력한다. 만약 정답이 없을 경우에는 -1을 출력한다.

# input 1
# 3 1

# output 1
# 1

# input 2
# 13 2

# output 2
# 3

# input 3
# 1000000 5

# output 3
# 15808

# n,k = map(int,input().split())
#
# left_water = n
#
# result_list = []
# def decreaseWater(n:int, k:int, buy_count:int, processCount:int):
#     processCount += 1
#     left_water = n // 2
#     check = n % 2
#
#     if left_water == 0:
#         return
#
#     if check == 1:
#         buy_count += (2 ** (processCount - 1))
#         left_water += 1
#
#     if check_count(left_water, 0) < k:
#         result_list.append(buy_count)
#
#     decreaseWater(left_water, k, buy_count, processCount)
#
# def check_count(input:int, count:int):
#     if input >= 2:
#         return check_count(input // 2, count + 1)
#
#     return count
#
# decreaseWater(n,k,0,0)
#
# print(min(result_list))


############풀이
# https://sosoeasy.tistory.com/119
# N,K=map(int,input().split())
#
#
# def cheak(num):
#     ans = 0
#     while (True):
#         a = num // 2        # 몫
#         b = num % 2         # 나머지
#         ans += b            # 나머지 물병
#         num = a
#         if num == 0:
#             break
#     return ans
#
#
# if K >= N:
#     print(0)
# else:
#     i = N
#     while (True):
#         if cheak(i) <= K:
#
#             print(i - N)
#             break
#         else:
#             i += 1


##########가장 직관적
# https://kimmeh1.tistory.com/304


import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
# print((bin(N)))
while bin(N).count('1') > K:
    # print(bin(N))
    plus = 2 ** (bin(N)[::-1].index('1'))
    # print(plus)
    answer += plus
    N += plus
print(answer)