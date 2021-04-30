# Example 1:
import heapq

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

# Output: 200
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.


# Example 2:

# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0

# Output: 500

# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
import collections
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        print(graph)

        # cost, 정점, 경유지
        Q = [(0, src, K)]

        while Q:
            cost, node, k = heapq.heappop(Q)
            if node == dst:
                return cost
            if k >= 0:
                for v,w in graph[node]:
                    alt = cost + w
                    heapq.heappush(Q, (alt, v ,k-1))

        return -1

# 커밋테스트야~
print(Solution().findCheapestPrice(n,edges,src,dst,k))