# prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

prices = [3, 2, 6, 5, 0, 3]

# prices = [1,2]
from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left, right = 0, len(prices)-1
#         left_value,right_value = prices[left], prices[right]
#         while left <= right:
#             # print(left, right)
#             left_value = min(left_value, prices[left])
#             right_value = max(right_value, prices[right])
#             print(left_value, right_value)
#             left +=1
#             right -=1
#
#         result = right_value - left_value
#         if result < 0:
#             return 0
#         return result
# print(Solution().maxProfit(prices))

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left_value,right_value = prices[0], prices[len(prices) - 1]
#         result = 0
#         for i in range(len(prices) -1):
#             left_value = min(prices[:i+1])
#             # print('left - {}'.format(prices[:i+1]))
#             right_value = max(prices[i+1:])
#             # print('right - {}'.format(prices[i+1:]))
#             result = max(result, right_value - left_value)
#
#         return result
#
# print(Solution().maxProfit(prices))

import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_value = sys.maxsize

        for price in prices:
            min_value = min(price, min_value)
            profit = max(profit, price - min_value)
        return profit

print(Solution().maxProfit(prices))
