# https://leetcode.com/problems/trapping-rain-water/

# 빗물 트래핑

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
