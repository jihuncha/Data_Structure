# Given a linked list, swap every two adjacent nodes and return its head.
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         cur = head
#
#         while cur and cur.next:
#             cur.val, cur.next.val = cur.next.val, cur.val
#             cur = cur.next.next
#
#         return head

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑값을 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head