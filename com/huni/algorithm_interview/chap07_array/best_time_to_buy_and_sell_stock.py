# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 주식을 사고 팔기 가장 좋은 시간

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
import sys

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [1,2]

from typing import List

# 시간 최악..
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        save_count = []
        hold_value = prices[0]

        for i in range(len(prices) - 1):
            if hold_value < prices[i + 1]:
                save_count.append(prices[i+1] - hold_value)
            else:
                hold_value = prices[i+1]
        # print(save_count)

        if not save_count:
            return 0
        else:
            return max(save_count)

        # for i in range(len(prices) - 1):
        #     if hold_value < prices[i+1]:
        #         count += 1
        #     else:
        #         hold_value = prices[i+1]
        #         save_count.append(count)
        #         count = 0
        #     if i + 1 == len(prices) - 1 and hold_value < prices[-1]:
        #         count += 1
        #         save_count.append(count)
        # if not save_count:
        #     return 0
        #
        # if max(save_count) == 0:
        #     return 0
        # else:
        #     return max(save_count)



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

print(Solution().maxProfit(prices))