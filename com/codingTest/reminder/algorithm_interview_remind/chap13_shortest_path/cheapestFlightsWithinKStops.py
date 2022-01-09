# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# There are n cities connected by some number of flights.
#
# You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

from typing import List

n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1

# Output: 200
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

# n = 3
# flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src = 0
# dst = 2
# k = 0


# Output: 500
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

# Constraints:
#
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst

# Wrong

# n = 4
# flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
# src = 0
# dst = 3
# k = 1
#
# Output: 6

n = 5
flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2

# Output: 7

# 시간초과까지.

# n = 13
# flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
# src = 10
# dst = 1
# k = 10

import heapq
import collections

# https://github.com/onlybooks/algorithm-interview/issues/104

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e9)

        graph = [[] for _ in range(n)]

        for check in flights:
            graph[check[0]].append((check[1], check[2]))

        # print(graph)

        distance = [INF] * n

        # visited = [False] * n

        # distance = [[INF] for _ in range(n)]
        # print(distance)

        def dijkstra(start):
            h = []
            distance[start] = 0
            # visited[start] = True
            # 거리 , index, 잔여 경유횟수
            heapq.heappush(h, (0, start, k))

            while h:
                dist, now, temp_k = heapq.heappop(h)

                if now == dst:
                    break

                if temp_k >= 0:
                    for temp in graph[now]:
                        # if visited[temp[0]]:
                        #     continue
                        # visited[temp[0]] = True
                        cost = dist + temp[1]
                        if cost < distance[temp[0]]:
                            distance[temp[0]] = cost
                        heapq.heappush(h, (cost, temp[0], temp_k - 1))

        dijkstra(src)
        # print(distance)

        return distance[dst] if distance[dst] != INF else -1

        # INF = int(1e9)
        #
        # graph = [[] for _ in range(n)]
        #
        # for check in flights:
        #     graph[check[0]].append((check[1], check[2]))
        #
        # # print(graph)
        #
        # distance = [INF] * n
        #
        # visited = [[] for _ in range(k+2)]
        #
        # # distance = [[INF] for _ in range(n)]
        # # print(distance)
        #
        # def dijkstra(start, k):
        #     h = []
        #     distance[start] = 0
        #     # 10번에 0번쨰로 방문
        #     visited[k+1][start] = 0
        #     # 거리 , index, 잔여 경유횟수
        #     heapq.heappush(h, (0, start, k))
        #
        #     while h:
        #         dist, now, temp_k = heapq.heappop(h)
        #
        #         if now == dst:
        #             break
        #
        #         if temp_k >= 0:
        #             for temp in graph[now]:
        #                 if temp[0] not in visited[temp_k]:
        #                     cost = dist + temp[1]
        #                     if cost < distance[temp[0]]:
        #                         distance[temp[0]] = cost
        #                     heapq.heappush(h, (cost, temp[0], temp_k - 1))
        #
        # dijkstra(src, k)
        # # print(distance)
        #
        # return distance[dst] if distance[dst] != INF else -1
        # # return distance



    # 플로이드?
    # graph = [[INF] * (n + 1) for _ in range(n + 1)]
    #
    # for i in range(1, n + 1):
    #     for j in range(1, n + 1):
    #         if i == j:
    #             graph[i][j] = 0
    #
    # for check in flights:
    #     graph[check[0]][check[1]] = check[2]
    # print(graph)
    #
    # for c in range(1, n + 1):
    #     for a in range(1, n + 1):
    #         for b in range(1, n + 1):
    #             graph[a][b] = min(graph[a][b], graph[a][c], graph[c][b])

    # print(graph)
    # print(graph[src][dst])


print(Solution().findCheapestPrice(n, flights, src, dst, k))

## 아무리해도 이해가안감...내껀왜안되??
## 책 정답도 타임아웃이였다 ㅋㅋㅋㅋ

import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         INF = int(1e9)
#
#         graph = [[] for _ in range(n)]
#
#         for check in flights:
#             graph[check[0]].append((check[1], check[2]))
#
#         # print(graph)
#
#         distance = [[INF] for _ in range(n)]
#         # print(distance)
#
#         def dijkstra(start):
#             h = []
#             distance[start] = [0]
#             # 거리 , index, 잔여 경유횟수
#             heapq.heappush(h, (0, start, k))
#
#             while h:
#                 dist, now, temp_k = heapq.heappop(h)
#
#                 if now == dst:
#                     break
#
#                 if temp_k >= 0:
#                     for temp in graph[now]:
#                         cost = dist + temp[1]
#                         # if cost < distance[temp[0]]:
#                         distance[temp[0]].append(cost)
#                         heapq.heappush(h, (cost, temp[0], temp_k-1))
#
#         dijkstra(src)
#         print(distance)
#
#         return min(distance[dst]) if min(distance[dst]) != INF else -1

print(Solution().findCheapestPrice(n,flights,src,dst,k))
