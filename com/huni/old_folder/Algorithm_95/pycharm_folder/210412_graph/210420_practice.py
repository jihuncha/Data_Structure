# https://leetcode.com/problems/permutations/
import itertools
from typing import List

# Example 1:
#
nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # def dfs(sum:int, data:List):
        #     # print(data)
        #     if sum > target:
        #         return
        #     if sum == target:
        #         temp = sorted(data)
        #         if temp not in result:
        #             result.append(temp)
        #         return
        #
        #     for i in candidates:
        #         data.append(i)
        #         dfs(sum + i, data)
        #         data.remove(i)
        #
        # dfs(0,[])
        # return result

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum ==0:
                result.append(path)
                return
            # index 로 하위원소만 체크..
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # print(nums.index(2))
        # def dfs(elements, temp:int):
        #     result.append(elements[:])
        #
        #     if len(elements) == len(nums):
        #         return
        #
        #     for i in range(temp, len(nums)):
        #         elements.append(i)
        #         dfs(elements, temp + 1)
        #         elements.remove(i)
        #
        # dfs([], 0)
        # return result

        def dfs(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0,[])
        return result

# print(Solution().permute(nums))

# Example 1:
#
# n = 4
# k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]

# print(Solution().combine(n,k))



# Example 1:
#
# candidates = [2,3,6,7]
# target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
#
# Input: candidates = [2], target = 1
# Output: []
# Example 4:
#
# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:
#
# Input: candidates = [1], target = 2
# Output: [[1,1]]


# print(Solution().combinationSum(candidates,target))


# Example 1:
#
nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]

print(Solution().subsets(nums))

# print(type(nums.index(2)))