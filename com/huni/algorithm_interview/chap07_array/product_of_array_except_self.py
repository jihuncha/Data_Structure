# https://leetcode.com/problems/product-of-array-except-self/

# 자기 자신을 제외한 배열의 곱

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

from typing import List

# 시간 초과
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result_list = []
#
#         for i in range(len(nums)):
#             temp_list = nums[i+1:] + nums[:i]
#             temp = 1
#             for j in temp_list:
#                 temp *= j
#             result_list.append(temp)
#
#         return result_list

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = []
        left_list = []
        right_list = []

        # left_list.append(1)
        temp = 1
        for i in range(0, len(nums)):
            left_list.append(temp)
            temp = temp * nums[i]
        print(left_list)

        temp = 1
        for j in range(len(nums) - 1, -1, -1):
            print(j)
            right_list.append(temp)
            temp = temp * nums[j]
        print(right_list)
        right_list.reverse()

        for i in range(0, len(nums)):
            result_list.append(left_list[i] * right_list[i])
        return result_list

print(Solution().productExceptSelf(nums))