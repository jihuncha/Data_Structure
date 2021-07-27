import sys

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
# prices = [1,2]

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_num = prices[0]
        count = 0

        for i in range(1, len(prices)):
            temp_num = min(temp_num, prices[i])
            count = max(count, prices[i] - temp_num)

        return count



        # result_list = []
        # temp_num = prices[0]
        # count = 0
        #
        # for i in range(len(prices) - 1):
        #     print(i, i+1)
        #     if temp_num < prices[i + 1]:
        #         count += 1
        #     else:
        #         result_list.append(count)
        #         temp_num = prices[i + 1]
        #         count = 0
        #
        # if count != 0:
        #     result_list.append(count)
        #
        # print(result_list)

print(Solution().maxProfit(prices))

# 빗물 트래핑

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9

from typing import List

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left = 0
#         right = len(height) - 1
#
#         while not left == right:
#             top_left = max(height[:left+1])
#             top_right = max(height[right:])
#             if top_left >= top_right:

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        count = 0