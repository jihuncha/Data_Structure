# Example 1:
#
# Input:
import collections

numCourses = 2
prerequisites = [[1, 0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = collections.defaultdict(list)
        # for i in prerequisites:
        #     if i[0] not in dic:
        #         dic[i[0]] = [i[1]]
        #     else:
        #         dic[i[0]].append(i[1])
        for x, y in prerequisites:
            dic[x].append(y)

        traced = set()

        def dfs(i):
            # 순환구조이면 False
            if i in traced:
                return False

            traced.add(i)

            for y in dic[i]:
                if not dfs(y):
                    return False

            traced.remove(i)

            return True

        for x in list(dic):
            if not dfs(x):
                return False

        return True

        # print(dic)


print(Solution().canFinish(numCourses, prerequisites))