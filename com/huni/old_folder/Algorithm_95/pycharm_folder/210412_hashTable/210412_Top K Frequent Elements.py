import heapq
from typing import List

# Example 1:
#
nums = [1,1,1,2,2,3]
k = 2
#
# Output: [1,2]
#
# Example 2:
#
# nums = [1]
# k = 1
# Output: [1]

import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 내풀이
        # count = collections.Counter(nums)
        # count.most_common(k)
        # result_list = []
        # for i in count.most_common(k):
        #     result_list.append(i[0])
        #
        # # print(result_list)
        #
        # return result_list

        #most_common 모르는 전제
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            print((-freqs[f],f))
            # key에 값을 대입 -> 최소힙만 지원 / 힙은 key순서대로 정렬되기떄문
            heapq.heappush(freqs_heap, (-freqs[f],f))

        topk = list()

        for _ in range(k):
            topk.append((heapq.heappop(freqs_heap)[1]))

        return topk

        #한줄풀이
        # return list(zip(*collections.Counter(nums).most_common(k)))[0]

print(Solution().topKFrequent(nums, k))