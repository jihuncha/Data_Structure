# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.
#
# If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

# T = [73, 74, 75, 71, 69, 72, 76, 73]
from typing import List


# 시간초과
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         stack = []
#         check = False
#
#         for i in range(len(T)):
#             check = False
#             for j in range(i, len(T)):
#                 if T[i] < T[j]:
#                     check = True
#                     stack.append(j-i)
#                     break
#             if not check:
#                 stack.append(0)
#
#         return stack

# 시간초과
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         stack = []
#         check = False
#
#         for i in range(len(T)):
#             # check = False
#             for j in range(i, len(T)):
#                 if max(T[j:]) <= T[i]:
#                     stack.append(0)
#                     break
#                 if T[i] < T[j]:
#                     check = True
#                     stack.append(j - i)
#                     break
#         return stack

T = [73, 74, 75, 71, 69, 72, 76, 73]
# T = [75, 71,69,72,76]
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            print(i, cur,stack)
            while stack and cur > T[stack[-1]]:
                print(T[stack[-1]])
                # print(stack)
                # print(cur, T[stack[-1]])
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        print(stack)
        return answer

print(Solution().dailyTemperatures(T))
