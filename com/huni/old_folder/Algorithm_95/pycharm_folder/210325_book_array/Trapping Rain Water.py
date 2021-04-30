# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9

height = [4,2,0,3,2,5]
# 풀이자체가 떠오르지않음..
from typing import List

# 두 포인터 최대로 이용
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
#
#         volume = 0
#         left, right = 0, len(height) - 1
#         left_max, right_max = height[left], height[right]
#
#         while left < right:
#             print('left - {}, right - {}'.format(left, right))
#             left_max, right_max = max(height[left], left_max), max(height[right], right_max)
#             print('left_max - {}, right_max - {}'.format(left_max, right_max))
#
#             if left_max <= right_max:
#                 volume += left_max - height[left]
#                 left += 1
#             else:
#                 volume += right_max - height[right]
#                 right -=1
#         return volume
#
# print(Solution().trap(height))


# stack 에 쌓기

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            print("cycle - " , i)
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                print("{} and {}".format(height[i], height[stack[-1]]))
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume
print(Solution().trap(height))
