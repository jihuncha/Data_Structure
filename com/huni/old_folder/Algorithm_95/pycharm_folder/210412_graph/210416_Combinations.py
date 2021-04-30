
# Example 1:
#
import itertools
from typing import List

n = 4
k = 2
# Output:
# [
#     [2 ,4],
#     [3 ,4],
#     [2 ,3],
#     [1 ,2],
#     [1 ,3],
#     [1 ,4],
# ]
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(itertools.combinations(range(1,n+1),k))
        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([],1,k)
        return result


print(Solution().combine(n,k))
