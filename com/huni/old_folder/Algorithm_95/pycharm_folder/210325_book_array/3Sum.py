from typing import List

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Input: nums = []
# Output: []

# Input: nums = [0]
# Output: []

nums = [-1,0,1,2,-1,-4]

# nums = [0,0,0]

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result_list = list(set(nums))
#         # print(result_list)
#
#         temp_list = []
#
#         for i in range(len(result_list)):
#             for j in range(i+1, len(result_list)):
#                 for k in range(i+2, len(result_list)):
#                     if result_list[i] + result_list[j] + result_list[k] == 0:
#                         result = [result_list[i],result_list[j],result_list[k]]
#                         result.sort()
#                         print(result)
#                         if result not in temp_list:
#                             temp_list.append(result)
#
#         # print(temp_list)
#         # for a in range(len(nums)):
#         #     for b in range(len(nums)):
#         #         for c in range(len(nums)):
#         #             if nums[a] + nums[b] + nums[c] == 0:
#         #
#         #
#         # if len(result_list) != 0:
#         #     return result_list
#         # else:
#         #     return list()
#
#
# print(Solution().threeSum(nums))

# timeout
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         nums.sort()
#
#         for i in range(len(nums) -2):
#             # 중복값 건너 뛰기
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i + 1, len(nums) -1):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 for k in range(j + 1, len(nums)):
#                     if k > j + 1 and nums[k] == nums[k - 1]:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result.append([nums[i], nums[j], nums[k]])
#
#
#         return result
#
# print(Solution().threeSum(nums))


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복값 건너 뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right -1]:
                        right -=1

                    left+=1
                    right-=1

        return result


print(Solution().threeSum(nums))
