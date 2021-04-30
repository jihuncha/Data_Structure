# Definition for singly-linked list.

head = [1,2,3,4,5]
Output: [5,4,3,2,1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

temp_head = ListNode(head[0])

for i in range(1, len(head)):
    temp_head.next = ListNode(head[i])
    temp_head = temp_head.next

# head_temp = ListNode(head[0])
# tail = head_temp
#
# e = 1
# while e < len(head):
#     # print(head_temp)
#     tail.next = ListNode(head[e])
#     tail = tail.next
#     e += 1
l1 = [2,4,3]
l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

temp_l1 = ListNode(l1[0])

for i in range(1, len(l1)):
    temp_l1.next = ListNode(l1[i])
    temp_l1 = temp_l1.next

temp_l2 = ListNode(l2[0])

for i in range(1, len(l2)):
    temp_l2.next = ListNode(l2[i])
    temp_l2 = temp_l2.next

list1 = [2,4,3]
head_temp = ListNode(list1[0])
tail = head_temp

e = 1
while e < len(list1):
    print(head_temp)
    tail.next = ListNode(list1[e])
    tail = tail.next
    e+=1

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # node, prev = head, None
        #
        # while node:
        #     next_data, node.next = node.next, prev
        #     prev, node = node, next_data
        #
        # return prev

        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next_data, node.next = node.next, prev
            return reverse(next_data, node)
        return reverse(head)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list, l2_list = [],[]
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        result_list = []
        # result_node = ListNode(None)
        carry = 0
        while l1_list or l2_list or carry:
            temp = l1_list.pop() + l2_list.pop() + carry
            if temp >= 10:
                temp -= 10
                carry = 1
            else:
                carry = 0

            result_list.append(temp)
            # result_node.next = ListNode(temp)
            # result_node = result_node.next

        result_node = ListNode(None)
        for i in range(len(result_list)):
            node = ListNode(result_list[i])
            node.next = result_node
            result_node = node

        return result_node
        # print(l1_list)
# print(Solution().reverseList(temp_head))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

print(Solution().addTwoNumbers(temp_l1,temp_l2))