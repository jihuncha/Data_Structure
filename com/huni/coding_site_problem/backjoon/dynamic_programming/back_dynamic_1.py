# https://www.acmicpc.net/problem/14501

# 퇴사

# 문제
# 상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
#
# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
#
# 백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
#
# 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
#
# N = 7인 경우에 다음과 같은 상담 일정표를 보자.
#
#  	1일	2일	3일	4일	5일	6일	7일
# Ti	3	5	1	1	2	4	2
# Pi	10	20	10	20	15	40	200
# 1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.
#
# 상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다.
#
# 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
#
# 또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
#
# 퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
#
# 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
#
# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)
#
# 출력
# 첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
#
# 예제 입력 1
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
#
# 예제 출력 1
# 45
#
# 예제 입력 2
# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10
#
# 예제 출력 2
# 55
#
# 예제 입력 3
# 10
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
#
# 예제 출력 3
# 20
#
# 예제 입력 4
# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50
#
# 예제 출력 4
# 90

#############################################
#### 겨우겨우..
#### d[i] = max(d[i-ti] + d[i], d[before??]])

data_len = int(input())

data = []
for insert_data in range(data_len):
    a,b = map(int,input().split())
    data.append((a,b))

# [(3, 10), (5, 20), (1, 10), (1, 20), (2, 15), (4, 40), (2, 200)]
# print(data)

# 결과 담는 리스트
result_list = [0] * data_len

# 뒤에서 부터 확인
for check in range(data_len-1, -1,-1):
    # 지나야하는 날짜 + 현재 날짜가 데이터 범위에 포함되어 있으면.
    if data[check][0] + check - 1 <= data_len - 1:
        # max값은 현재 값 // 현재에서 지나야하는 날짜 이후 부터의 max 값 + 현재 값
        # 뒷부분은 범위 벗어나는거 방지하기 위한 예외처리 -> 현재값으로
        max_result = max(data[check][1], max(result_list[check+data[check][0]:]) + data[check][1]) \
            if check + data[check][0] <= data_len - 1 else data[check][1]
    else:
        # 범위에 해당 되지 않는 경우는 0으로
        max_result = 0
    # 값 갱신
    result_list[check] = max_result

print(max(result_list))


##### 풀이
# n = int(input())
# t = []
# p = []
# dp = [0] * (n + 1)
# max_value = 0
#
# for _ in range(n):
#     x,y = map(int, input().split())
#     t.append(x)
#     p.append(y)
#
# for i in range(n-1, -1, -1):
#     time = t[i] + i
#
#     if time <= n:
#         dp[i] = max(p[i] + dp[time], max_value)
#         max_value = dp[i]
#
#     else:
#         dp[i] = max_value
#
# print(max_value)

# def check_max_value(idx: int):
#     # print("check_max_value", idx,data_len)
#     index = idx
#     left_count = data[idx][0]
#     result = 0
#     last = data[idx][1]
#     while index < data_len:
#         if left_count == 0:
#             result += last
#             temp = data[index]
#             left_count = temp[0]
#             last = temp[1]
#         left_count -= 1
#         index += 1
#         # if left_count != 0:
#         #     result -= last
#
#         # print(left_count)
#     #     print("check", index, left_count)
#     #     left_count -= 1
#     #
#     #     if left_count == 0 or index == idx:
#     #         temp = data[index]
#     #         left_count = temp[0]
#     #         last = temp[1]
#     #         result += last
#     #         print(result)
#     #     index += 1
#     # if left_count != 0:
#     #     result -= last
#     #
#     result_list.append(result)
#
# # print(result)
# for i in range(data_len):
#     check_max_value(i)
#
# print(result_list)
# print(max(result_list))
