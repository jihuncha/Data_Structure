# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # odd_result,even_result = ListNode(None),ListNode(None)
        #
        # while head:
        #     if head.val % 2 == 1:
        #         odd_result.next = ListNode(head)
        #         odd_result = odd_result.next
        #     else:
        #         even_result.next = ListNode(head)
        #         even_result = even_result.next
        #
        #     head = head.next
        #     odd_result.next = even_result
        # return odd_result
        if head is None:
            return None

        # 인덱스가 짝수 홀수
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 반복 과정 수행 이후 even head를 odd.next 와 연결
        odd.next = even_head
        return head

list1 = [1,2,3,4,5]
head_temp = ListNode(list1[0])
tail = head_temp

e = 1
while e < len(list1):
    # print(head_temp)
    tail.next = ListNode(list1[e])
    tail = tail.next
    e += 1

print(Solution().oddEvenList(head_temp))