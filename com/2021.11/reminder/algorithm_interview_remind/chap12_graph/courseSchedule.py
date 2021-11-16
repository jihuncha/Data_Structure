# https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

numCourses = 2
prerequisites = [[1,0]]
#
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

numCourses = 2
prerequisites = [[1,0],[0,1]]
#
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

numCourses = 3
prerequisites = [[1,0],[0,2],[1,2],[2,1]]

# Constraints:
#
# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


from typing import List

from collections import defaultdict


### 이해를 잘 못해서 못품 ㅠ
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1 or len(prerequisites) <= 1:
            return True

        dic = defaultdict()
        for data in prerequisites:
            if data[0] not in dic:
                dic[data[0]] = [data[1]]
            else:
                dic[data[0]].append(data[1])

        print(dic)

        visited = [False for _ in range(numCourses)]
        print(visited)

        def dfs(index:int, my_list:list, visited_list:list):
            print(visited, index, visited_list)
            if index in my_list:
                return False

            if visited:
                return True

            for i in my_list:
                dfs(i, dic[i])


        for i in range(numCourses):
            dfs(i, dic[i], visited)


        return True

#############
# 순환 구조

# 풀이 1.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)

        for i in prerequisites:
            dic[i[0]].append(i[1])
        # print(dic)

        # 방문한 곳을 재 방문 = 순환이다 -> False로 간주
        traced = set()
        
        visited = set()

        def dfs(num:int):
            # 순환구조 체크
            if num in traced:
                return False
            
            # 방문한경우
            if num in visited:
                return True

            traced.add(num)
            for y in dic[num]:
                if not dfs(y):
                    return False
            # 탐색 종료
            traced.remove(num)

            # 종료이후 visited 추가해준다
            visited.add(num)

            return True

        for j in range(numCourses):
            if not dfs(j):
                return False

        return True

        

print(Solution().canFinish(numCourses, prerequisites))