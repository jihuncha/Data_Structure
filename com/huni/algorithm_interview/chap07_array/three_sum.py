# https://leetcode.com/problems/3sum/

# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
#
# Input: nums = []
# Output: []
#
# Example 3:
#
# Input: nums = [0]
# Output: []

nums = [-1,0,1,2,-1,-4]
# nums = []
# nums = [0]

import itertools
from typing import List


# 시간 초과
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        index_list = [i for i in range(len(nums))]
        temp = list(itertools.combinations(index_list, 3))

        result = []
        for i in temp:
            a,b,c = i
            if nums[a] + nums[b] + nums[c] == 0:
                temp_result = list([nums[a],nums[b],nums[c]])
                temp_result.sort()
                if temp_result not in result:
                    result.append(temp_result)
        return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right = i + 1, len(nums) - 1

            while left < right:
                sum_result = nums[i] + nums[left] + nums[right]
                if sum_result < 0:
                    left += 1
                elif sum_result > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left],nums[right]])

                    # 동일값 만큼 이동..
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    # 그 다음 값
                    left +=1
                    right -= 1
        return results

print(Solution().threeSum(nums))