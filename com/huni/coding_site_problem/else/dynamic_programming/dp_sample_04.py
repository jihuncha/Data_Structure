# https://www.acmicpc.net/problem/18353

# 병사 배치

# 문제
# N명의 병사가 무작위로 나열되어 있다. 각 병사는 특정한 값의 전투력을 보유하고 있으며, 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록
# 내림차순으로 배치를 하고자 한다. 다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다.
#
# 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다. 그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶다.
#
# 예를 들어, N=7일 때 나열된 병사들의 전투력이 다음과 같다고 가정하자.
#
#
#
# 이 때 3번 병사와 6번 병사를 열외시키면, 다음과 같이 남아있는 병사의 수가 내림차순의 형태가 되며 5명이 된다. 이는 남아있는 병사의 수가 최대가 되도록 하는 방법이다.
#
#
#
# 병사에 대한 정보가 주어졌을 때, 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 2,000) 둘째 줄에 각 병사의 전투력이 공백을 기준으로 구분되어 차례대로 주어진다. 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수를 출력한다.
#
# 7
# 15 11 4 8 5 2 4

# 2

import bisect

n = int(input())

data = list(map(int, input().split()))

data.reverse()
# print(data)

dp = [1] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
# stack = [data[0]]
#
# for i in range(1, n):
#     if stack[-1] < data[i]:
#         stack.append(data[i])
#     else:
#         index = bisect.bisect_left(stack, data[i])
#         stack[index] = data[i]

# print(stack)

# print(n - len(stack))