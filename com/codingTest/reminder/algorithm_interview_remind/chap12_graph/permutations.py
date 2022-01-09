# https://leetcode.com/problems/permutations/
import itertools

nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# nums = [0,1]

# Output: [[0,1],[1,0]]



# nums = [1]

# Output: [[1]]






from typing import List

#1. dfs
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result_list = []

        def dfs(my_list:List, temp_list:List):
            if len(my_list) == len(nums):
                # 주소값 복사를 방지하기 위함
                result_list.append(my_list[:])
                return

            for i in range(len(temp_list)):
                my_list.append(temp_list[i])
                dfs(my_list, temp_list[i+1:] + temp_list[:i])
                my_list.remove(temp_list[i])

        dfs([], nums)

        return result_list


print(Solution().permute(nums))

#2. itertools 써볼까
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ##내용물이 튜플
        # return (list(permutations(nums)))

        return list(map(list, itertools.permutations(nums)))

        # result_list = []
        #
        # def dfs(my_list:List, temp_list:List):
        #     if len(my_list) == len(nums):
        #         # 주소값 복사를 방지하기 위함
        #         result_list.append(my_list[:])
        #         return
        #
        #     for i in range(len(temp_list)):
        #         my_list.append(temp_list[i])
        #         dfs(my_list, temp_list[i+1:] + temp_list[:i])
        #         my_list.remove(temp_list[i])
        #
        # dfs([], nums)

        # return result_list

print(Solution().permute(nums))


### 책 풀이
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         prev_elements = []
#
#         def dfs(elements):
#             # 리프 노드일때 결과 추가
#             if len(elements) == 0:
#                 results.append(prev_elements[:])
#
#             # 순열 생성 재귀 호출
#             for e in elements:
#                 next_elements = elements[:]
#                 next_elements.remove(e)
#
#                 prev_elements.append(e)
#                 dfs(next_elements)
#                 prev_elements.pop()
#
#         dfs(nums)
#         return results