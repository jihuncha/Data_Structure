# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: l1 = [], l2 = []
# Output: []

# Input: l1 = [], l2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# temp = 0
# class Solution:
#
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         global temp
#         temp += 1
#
#         print("time - {}".format(temp))
#         # l1 이 없거나 / l2가 존재하면서 l2의 값이 더 적을 경우
#         if (not l1) or (l2 and l1.val > l2.val):
#             l1,l2 = l2,l1
#             print(l1.val, l2.val)
#             # print("next - {}, {}".format(l1.next.val, l2.next.val))
#         if l1:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1
#
#
# l1 = [1,2,4]
# l2 = [1,3,4]
# l1_temp = ListNode(l1[0])
# l2_temp = ListNode(l2[0])
# tail = l1_temp
# tail_second = l2_temp
#
# e = 1
# while e < len(l1):
#     # print(head_temp)
#     tail.next = ListNode(l1[e])
#     tail = tail.next
#     e+=1
#
# e = 1
# while e < len(l2):
#     # print(head_temp)
#     tail_second.next = ListNode(l2[e])
#     tail_second = tail_second.next
#     e+=1
#
# print(Solution().mergeTwoLists(l1_temp,l2_temp))
#

l1 = [1,2,4]
l2 = [1,3,4]
Output: [1,1,2,3,4,4]

# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

temp_l1 = ListNode(l1[0])
for i in range(1,len(l1)):
    temp_l1.next = ListNode(l1[i])
    temp_l1 = temp_l1.next

# print(temp_l1)

temp_l2 = ListNode(l2[0])
for i in range(1,len(l2)):
    temp_l2.next = ListNode(l2[i])
    temp_l2 = temp_l2.next

# print(temp_l2)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # result = ListNode()

        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            # print(l1.val)
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


temp = Solution().mergeTwoLists(temp_l1, temp_l2)

# while temp:
#     print(temp.val)
#     temp = temp.next

# print(Solution().mergeTwoLists(temp_l1, temp_l2))
