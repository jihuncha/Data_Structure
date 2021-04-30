from typing import List

nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# nums = [0, 1]
# Output: [[0, 1], [1, 0]]

# nums = [1]
# Output: [[1]]

# nums = [1,2,3,4]
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return (list(itertools.permutations(nums, len(nums))))
        # return list(map(list, itertools.permutations(nums, len(nums))))

        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일떄 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                print(next_elements)
                prev_elements.append(e)
                print("prev - ",prev_elements)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results
print(Solution().permute(nums))

