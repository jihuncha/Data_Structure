nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
from typing import List


# timeout
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(len(nums)):
#             count = 1
#             for idx, value in enumerate(nums):
#                 if i != idx:
#                     count *= value
#             result.append(count)
#
#         return result
#
# print(Solution().productExceptSelf(nums))

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        print('first - {}'.format(out))
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out

print(Solution().productExceptSelf(nums))
