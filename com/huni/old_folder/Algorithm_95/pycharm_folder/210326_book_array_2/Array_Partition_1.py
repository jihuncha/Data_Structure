from typing import List

nums = [1,4,3,2]
# Output: 4
#
# nums = [6,2,6,5,1,2]
# Output: 9

# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         result = 0
#         for i in range(len(nums)):
#             if i % 2 != 0:
#                 result += min(nums[i], nums[i-1])
#
#         return result
#
# print(Solution().arrayPairSum(nums))


# 파이선스러운
# 짝수번쨰가 항상 작은값이 되므로
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

print(Solution().arrayPairSum(nums))
