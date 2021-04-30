# You are given a network of n nodes,
# labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node,
# vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k.
# Return the time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.

# times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2
#
# Output: 2
#
#
# times = [[1,2,1]]
# n = 2
# k = 1
#
# Output: 1
#
#
# times = [[1,2,1]]
# n = 2
# k = 2
# Output: -1
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        # 큐 변수 : [(소요시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지의 최단 경로 삽입
        while Q:
            time, node =heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == n:
            return max(dist.values())
        return -1

