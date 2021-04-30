# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     #연결 리스트 뒤집기
#     def reverseList(self, head:ListNode) -> ListNode:
#
#         # [1,2,3,4,5]
#
#         node,prev = head, None
#
#         # [1,2,3,4,5]
#
#         while node:
#             # next에 다음 노드, 이전 노드에 다음노드 선언
#             next, node.next = node.next, prev
#             # 2, None
#             # 3, 1
#             # 4, 2
#             # 5, 3
#             # None, 4
#             prev, node = node,next
#             # 1, 2
#             # 2, 3
#             # 3, 4
#             # 4, 5
#             # 5, None
#         return prev
#
#     def toList(self, l1 : ListNode) -> List:
#         result = []
#         while l1:
#             result.append(l1.val)
#             l1 = l1.next
#         return result
#
#     def toListNode(self, l2 : List) -> ListNode:
#         prev: ListNode = None
#         for r in l2:
#             node = ListNode(r)
#             node.next = prev
#             prev = node
#         return node
#
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         a = self.toList(self.reverseList(l1))
#         b = self.toList(self.reverseList(l2))
#
#         resultStr = int(''.join(str(e) for e in a)) + \
#                     int(''.join(str(e) for e in b))
#
#         return self.toListNode(str(resultStr))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head= ListNode(0)

        carry = 0

        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next