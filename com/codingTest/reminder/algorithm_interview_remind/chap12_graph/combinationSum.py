# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
#
# You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
from typing import List

candidates = [2,3,6,7]
target = 7

# Output: [[2,2,3],[7]]
#
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

candidates = [2,3,5]
target = 8

# Output: [[2,2,2,2],[2,3,3],[3,5]]

candidates = [2]
target = 1

# Output: []

candidates = [1]
target = 1

# Output: [[1]]

Input: candidates = [1]
target = 2

# Output: [[1,1]]

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500

candidates = [2,3,6,7]
target = 7


## 내풀이
### 너무 느리다 ..  1408 ms

### 내가 뺴먹은것 - 조합이니까 index = 1로 검색한 이후에는 index=2부터 검색하면됨.. - sort작업이 불필요해짐
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []

        def dfs(input_list:List):
            if sum(input_list) == target:
                append_list = list(input_list[:])
                append_list.sort()
                if append_list not in result_list:
                    result_list.append(append_list)
                return

            # 합이 이미 target 보다 큰 경우 -> 그냥 빠져나간다.
            if sum(input_list) > target:
                return

            for i in range(len(candidates)):
                temp = list(input_list[:])
                temp.append(candidates[i])
                dfs(temp)
                temp.remove(candidates[i])

        dfs([])

        return result_list

print(Solution().combinationSum(candidates, target))

#책 풀이 	84 ms
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result_list.append(path)
                return

            # 자기부터 하위 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result_list

        # 내 재풀이
        # 132ms
        
        # def dfs(input_list:List, index:int):
        #     if sum(input_list) == target:
        #         append_list = list(input_list[:])
        #         # append_list.sort()
        #         if append_list not in result_list:
        #             result_list.append(append_list)
        #         return
        #
        #     # 합이 이미 target 보다 큰 경우 -> 그냥 빠져나간다.
        #     if sum(input_list) > target:
        #         return
        #
        #     for i in range(index, len(candidates)):
        #         temp = list(input_list[:])
        #         temp.append(candidates[i])
        #         dfs(temp, i)
        #         temp.remove(candidates[i])
        #
        # dfs([], 0)

        # return result_list

print(Solution().combinationSum(candidates, target))


