# s = "babad"
#
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand(start :int, end :int) -> str:
#             while start >= 0 and end < len(s) and s[start] == s[end]:
#                 start -= 1
#                 end += 1
#             return s[start + 1: end]
#
#         if len(s) < 2 or s[:] == s[::-1]:
#             return s
#
#         result = ''
#         for i in range(len(s) - 1):
#             result = max(result,
#                          expand(i, i+1),
#                          expand(i, i+2),
#                          key=len)
#
#         return result
#
# print(Solution().longestPalindrome(s))


# from typing import List
#
# nums = [2,7,11,15]
# target = 9
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         temp_dic = {}
#         for i in range(len(nums)):
#             if target - nums[i] in temp_dic:
#                 return [temp_dic[target - nums[i]],i]
#             temp_dic[nums[i]] = i
#
# print(Solution().twoSum(nums,target))
from typing import List

height = [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            print(left_max, right_max)

            if left_max <= right_max:
                print("left - {}".format(left_max - height[left]))
                volume += left_max - height[left]
                left += 1
            else:
                print("right - {}".format(right_max - height[right]))
                volume += right_max - height[right]
                right -= 1

        return volume

print(Solution().trap(height))