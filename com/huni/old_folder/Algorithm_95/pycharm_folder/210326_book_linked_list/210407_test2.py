from typing import List
#
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def toReversedLinkedList(result: str) -> ListNode:
#     prev: ListNode = None
#     for r in result:
#         node = ListNode(r)
#         node.next = prev
#         prev = node
#     return node
#
# test1 = '342'
# temp1 = toReversedLinkedList(test1)
#
# test2 = '465'
# temp2 = toReversedLinkedList(test1)
#
# # l1 = [2,4,3]
# #
# # l2 = [5,6,4]
# #
# # temp_l1 = ListNode(l1[0])
# #
# # for i in range(1, len(l1)):
# #     temp_l1.next = ListNode(l1[i])
# #     temp_l1 = temp_l1.next
# #
# # temp_l2 = ListNode(l2[0])
# #
# # for i in range(1, len(l2)):
# #     temp_l2.next = ListNode(l2[i])
# #     temp_l2 = temp_l2.next
#
#
#
# class Solution:
#     # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#     #     root = head = ListNode(0)
#     #
#     #     carry = 0
#     #     while l1 or l2 or carry:
#     #         sum = 0
#     #         if l1:
#     #             sum += int(l1.val)
#     #             l1 = l1.next
#     #         if l2:
#     #             sum += int(l2.val)
#     #             l2 = l2.next
#     #
#     #         carry, val = divmod(sum + carry, 10)
#     #         # print(carry, val)
#     #
#     #         head.next = ListNode(val)
#     #         head = head.next
#     #         # print(sum, carry, val)
#     #
#     #     return root.next
#
#     # def swapPairs(self, head: ListNode) -> ListNode:
#     #     # cur = head
#     #     #
#     #     # while cur and cur.next:
#     #     #     cur.val, cur.next.val = cur.next.val, cur.val
#     #     #     cur = cur.next.next
#     #     #
#     #     # return head
#     #
#     #     root = prev = ListNode(None)
#     #     # 이전것의 다음것은 현재 걸로 미리 설정(?)
#     #     # none.next -> 1
#     #     prev.next = head
#     #
#     #     # 1. 2
#     #     while head and head.next:
#     #         # b= 2
#     #         b = head.next
#     #         # 1의 next - 3
#     #         head.next = b.next
#     #         # 3 에 2 대입
#     #         b.next = head
#     #         print(b.val)
#     #
#     #         # none next -2
#     #         prev.next = b
#     #
#     #         # 1 -> 2
#     #         head = head.next
#     #         # none -> 3
#     #         prev = prev.next.next
#             # sum, carry = divmod()
#     # def reverseList(self, head: ListNode):
#     #     node, prev = head, None
#     #
#     #     while node:
#     #         next, node.next = node.next, prev
#     #         prev, node = node, next
#     #
#     #     return prev
#     #
#     # def toList(self, node: ListNode) -> List:
#     #     list: List = []
#     #     while node:
#     #         list.append(node.val)
#     #         node = node.next
#     #     return list
#     #
#     # def toReversedLinkedList(self, result:str) -> ListNode:
#     #     prev: ListNode = None
#     #     for r in result:
#     #         node = ListNode(r)
#     #         node.next = prev
#     #         prev = node
#     #     return node
#     #
#     # def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
#     #     a = self.toList(self.reverseList(l1))
#     #     b = self.toList(self.reverseList(l2))
#     #
#     #     resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
#     #
#     #     return self.toReversedLinkedList(str(resultStr))
#
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         root = head
#         result = temp = ListNode(None)
#         odd_list,even_list = [],[]
#         index = 0
#         while root:
#             if index % 2 == 0:
#                 odd_list.append(root.val)
#             else:
#                 even_list.append(root.val)
#             root = root.next
#             index +=1
#
#         for i in odd_list:
#             temp.next = ListNode(i)
#             temp = temp.next
#
#         for i in even_list:
#             temp.next = ListNode(i)
#             temp = temp.next
#
#         return result.next
#
#
# # print(Solution().addTwoNumbers(temp1,temp2))
#
#
# test = [1,2,3,4]
# test2 = [1,3,5,6,7]
# #
# a = b = test
# b = test2
#
# print(id(a))
# print(id(b))
# print(id(test))
# #
# # print(a)
# # print(b)
# #
# # b[1] = 100
# #
# # print(a)
# # print(b)
# # print(test)
#
#
# result = temp = ListNode(0)
#
# temp.next = ListNode(10)
# print(id(result))
# print(id(temp))
# temp = temp.next
#
# # print(result.val)
# # print(temp.val)
# print(id(result))
# print(id(temp))
# # print(id())

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

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
#         root = head
#         temp, result = [], []
#         while head:
#             temp.append(head.val)
#             head = head.next
#         # print(sorted(temp[left:right+1],reverse=True))
#         # auth = sorted(temp[left-1:right], reverse=True)
#         # print(auth)
#         result = temp[0:left - 1] + temp[left - 1:right:][::-1] + temp[right:]
#         # print(result)
#
#         head = node = ListNode(None)
#         for i in result:
#             node.next = ListNode(i)
#             node = node.next
#         return head.next
#
#         # sorted()
#
# left,right = 1,10
# temp = [9,8,7,6,5,4,3,2,1,0]
# result = []
# print(temp[0:0])
# print(type(temp[left-1:right]))
# result = temp[0:left-1] + temp[left-1:right:][::-1] + temp[right:]
#
# print(result)