# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    #내 풀이
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # result_list = []
        # for i in lists:
        #     while i:
        #         result_list.append(i.val)
        #         i = i.next
        # # print(result_list)
        #
        # result_list.sort()
        # result_node = temp = ListNode(None)
        # for i in result_list:
        #     temp.next = ListNode(i)
        #     temp = temp.next
        # return result_node.next
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

