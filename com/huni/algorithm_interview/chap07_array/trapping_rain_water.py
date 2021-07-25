# https://leetcode.com/problems/trapping-rain-water/

# 빗물 트래핑

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
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

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        volume = 0

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max < right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만난 경우
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)


class Solution:
    def trap(self, height: List[int]) -> int:

        unit = 0

        for i in range(1, len(height) - 1):
            volumes = min(max(height[:i]), max(height[i:])) - height[i]
            if volumes > 0:
                unit += volumes

        return unit
# print(Solution().trap(height))
