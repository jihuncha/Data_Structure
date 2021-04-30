# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(left-1):
            start = start.next
        end = start.next

        #반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

list1 = [1,2,3,4,5]
head_temp = ListNode(list1[0])
tail = head_temp

e = 1
while e < len(list1):
    # print(head_temp)
    tail.next = ListNode(list1[e])
    tail = tail.next
    e += 1

print(Solution().reverseBetween(head_temp, 2, 4))




