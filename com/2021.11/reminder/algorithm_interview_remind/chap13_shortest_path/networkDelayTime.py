# https://leetcode.com/problems/network-delay-time/

# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
#
# Output: 2

times = [[1,2,1]]
n = 2
k = 1
#
# Output: 1

times = [[1,2,1]]
n = 2
k = 2
#
# Output: -1

from typing import List

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)

        graph = [[] for _ in range(n+1)]

        distance = [INF] * (n+1)

        for temp in times:
            graph[temp[0]].append((temp[1], temp[2]))

        def dijkstra(start):
            h = []
            distance[start] = 0

            heapq.heappush(h, (0, start))

            while h:
                dist, now = heapq.heappop(h)

                if distance[now] < dist:
                    continue

                for check in graph[now]:
                    cost = dist + check[1]
                    if cost < distance[check[0]]:
                        distance[check[0]] = cost
                        heapq.heappush(h, (cost, check[0]))

        dijkstra(k)

        result = max(distance[1:]) if max(distance[1:]) != INF else -1

        return result

print(Solution().networkDelayTime(times, n, k))


# 책풀이 좀 신선..

import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1

