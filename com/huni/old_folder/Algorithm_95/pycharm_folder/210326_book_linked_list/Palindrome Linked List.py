# Input: head = [1,2,2,1]
# Output: true
#
# head = [1,2]
# Output: false
# head : Li

# Definition for singly-linked list.
import collections
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# import collections
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         q: Deque = collections.deque()
#
#         if not head:
#             return True
#
#         node = head
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#
#         print(len(q))
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#
#         return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        #런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

# Input: head = [1,2,2,1]
# Output: true
# list1 = [1,2]
list1 = [1,2,2,1]
head_temp = ListNode(list1[0])
tail = head_temp

e = 1
while e < len(list1):
    print(head_temp)
    tail.next = ListNode(list1[e])
    tail = tail.next
    e+=1

print(Solution().isPalindrome(head_temp))