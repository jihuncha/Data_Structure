# Example 1:
#
import itertools

nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# nums = [1]
# Output: [[1]]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def dfs_sample():
        # return list(itertools.permutations(nums))

        result = []
        prev_leafs = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_leafs[:])

            for temp in elements:
                next_leafs = elements[:]
                next_leafs.remove(temp)

                prev_leafs.append(temp)
                print("count 1 - ", prev_leafs)
                dfs(next_leafs)
                prev_leafs.pop()
                print("count 2 -", prev_leafs)



        dfs(nums)
        return result


print(Solution().permute(nums))

