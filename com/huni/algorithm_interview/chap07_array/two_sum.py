# https://leetcode.com/problems/two-sum/

# 두 수의 합

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Example 1:
#
nums = [2,7,11,15]
target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# nums = [3,3]
# target = 6
# Input: nums = [3,3], target = 6
# Output: [0,1]
import copy

# nums = [3,3]
# target = 6

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result_list = []
        # for idx in range(len(nums)):
        #     if target - nums[idx] in nums[idx+1:]:
        #         result_list = [idx, nums[idx+1:].index(target - nums[idx]) + (idx + 1)]
        # return result_list
        key_dic = {}
        for idx, i in enumerate(nums):
            if target - i in key_dic:
                return [key_dic[target - i], idx]
            key_dic[i] = idx
print(Solution().twoSum(nums, target))