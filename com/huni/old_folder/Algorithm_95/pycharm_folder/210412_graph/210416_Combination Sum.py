from typing import List

# Example 1:

candidates = [2,3,6,7]
target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
#
candidates = [2,3,5]
target = 8
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

candidates = [1,2]
target = 4

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # result = []
        #
        # def dfs(elements, prev_node):
        #     sum_result = sum(prev_node)
        #
        #     if sum_result > target:
        #         return
        #
        #     if sum_result == target:
        #         # prev_node.sort()
        #         temp = sorted(prev_node)
        #         if temp not in result:
        #             result.append(temp)
        #         return
        #     for i in elements:
        #         prev_node.append(i)
        #         print(prev_node)
        #         dfs(elements, prev_node)
        #         prev_node.pop()
        #
        # dfs(candidates,[])
        # return result

        result = []
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])


        dfs(target, 0, [])
        return result


print(Solution().combinationSum(candidates,target))