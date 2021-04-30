# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Input: head = [1,2]
# Output: [2,1]
#
# Input: head = []
# Output: []


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev



list1 = [1,2,3,4,5]
head_temp = ListNode(list1[0])
tail = head_temp

e = 1
while e < len(list1):
    # print(head_temp)
    tail.next = ListNode(list1[e])
    tail = tail.next
    e += 1

print(Solution().reverseList(head_temp))