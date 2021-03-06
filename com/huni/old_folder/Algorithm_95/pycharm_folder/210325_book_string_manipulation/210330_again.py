#1. palindrome

# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.


import collections
from typing import Deque, List, re

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # deque: Deque = collections.deque()
#         q = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 q.append(char.lower())
#
#         print(q)
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#         return True
#
# print(Solution().isPalindrome(s))


###########################################################################################################################################
# Example 1:
#
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
# Example 2:
#
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         letters, digits = [],[]
#         print(logs)
#
#         for check_all in logs:
#             if check_all.split()[1].isdigit():
#                 digits.append(check_all)
#             else:
#                 letters.append(check_all)
#
#         letters.sort(key=lambda x: [x.split()[1:], x.split()[0]])
#
#         return letters + digits
#
# print(Solution().reorderLogFiles(logs))

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:
#
# Input: paragraph = "a.", banned = []
# Output: "a"

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# 
# import re
# import collections
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
#             .lower().split()
#             if word not in banned]
#         # print(words)
# 
#         print(collections.Counter(words).most_common(1))
# 
# Solution().mostCommonWord(paragraph, banned)

# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]

# strs = ["eat","tea","tan","ate","nat","bat"]
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dic = {}
#
#         for i in strs:
#             temp_str = ''.join(sorted(i))
#             print(temp_str)
#             if temp_str not in dic:
#                 dic[temp_str] = [i]
#             else:
#                 dic[temp_str].append(i)
#         return list(dic.values())
#
#
# print(Solution().groupAnagrams(strs))

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"

# import collections
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         collections.deque =

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# s = "babad"
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         m = ''
#         for i in range(len(s)):
#             for j in range(len(s), i,-1):
#                 if len(m) >= j - i:  # To reduce time
#                     break
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m
#
# print(Solution().longestPalindrome(s))

# s = "abcdedcbabs"
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         print(s[0:8])
#         def expand(left : int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 print(s[left], s[right])
#                 left -= 1
#                 right += 1
#             print("expand_result - {}".format(s[left+1:right]))
#             return s[left + 1:right]
#
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         result = ''
#         # index ?????? -1 ??????
#         for i in range(len(s) - 1):
#             result = max(result, expand(i, i+1), expand(i, i+2), key=len)
#             print("i - {}, result - {}".format(i, result))
#         return result
#
# print(Solution().longestPalindrome(s))

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
height = [4,2,0,3,2,5]
# Output: 9

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         stack = []
#         volume = 0
#
#         for i in range(len(height)):
#             while stack and height[i] > height[stack[-1]]:
#                 top = stack.pop()
#
#                 if not len(stack):
#                     break
#
#                 # ??? ???????????? ???????????? ??? ?????? ???????
#                 distance = i - stack[-1] -1
#                 waters = min(height[i], height[stack[-1]]) - height[top]
#
#                 volume += distance * waters
#
#             stack.append(i)
#         return volume
#
#
#         # if not height:
#         #     return 0
#         #
#         # left, right = 0, len(height) - 1
#         # left_max, right_max = height[left], height[right]
#         # volume = 0
#         #
#         # while left < right:
#         #     if left_max < right_max:
#         #         left += 1
#         #         if left_max - height[left] > 0:
#         #             volume += left_max - height[left]
#         #         left_max = max(left_max, height[left])
#         #     else :
#         #         right -= 1
#         #         if right_max - height[right] > 0:
#         #             volume += right_max - height[right]
#         #         right_max = max(right_max, height[right])
#         #
#         # return volume
#
# print(Solution().trap(height))

# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         nums.sort()
#
#         for i in range(len(nums) - 2):
#
#             # ????????? ?????? ??????
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#
#             left, right = i + 1, len(nums) - 1
#
#             while left < right:
#                 sum_all = nums[i] + nums[left] + nums[right]
#
#                 if sum_all < 0:
#                     left +=1
#                 elif sum_all > 0:
#                     right -=1
#                 else:
#                     result.append([nums[i],nums[left],nums[right]])
#
#                     # ?????? ???????????? ??????
#                     while left < right and nums[left] == nums[left + 1]:
#                         left +=1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -=1
#
#                     left +=1
#                     right-=1
#
#         return result

# print(Solution().threeSum(nums))

# nums = [-1,1,0,-3,3]
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = []
#         p = 1
#
#         for i in range(0,len(nums)):
#             result.append(p)
#             p = p * nums[i]
#
#         p = 1
#
#         for i in range(len(nums) - 1, 0 - 1, -1):
#             result[i] = result[i] * p
#             p = p * nums[i]
#
#         return result
#
# print(Solution().productExceptSelf(nums))



# ?????? ??????	????????? ??????	??????	??????	?????? ??????	?????? ??????
# 2 ???	128 MB	68947	35835	30407	52.057%
# ??????
# ?????? ?????? ?????? X??? ??? ????????? ??????????????? ????????????, ??? ?????? ???????????? ??????.
# ??????????????? ????????? ??? ?????? ?????? ????????? ????????? ????????? ?????????. N??? ???????????? ???, 1?????? ????????? ??????, N?????? ????????? ?????? ????????? ????????? ???????????? ??????????????? ???????????????.
# ??????
# ?????? ?????? 1,000?????? ????????? ?????? ????????? N??? ????????????.
#
# ??????
# ?????? ?????? 1?????? ????????? ??????, N?????? ????????? ?????? ????????? ????????? ????????????.

# ?????? ?????? 1
# 110
# ?????? ?????? 1
# 99
# ?????? ?????? 2
# 1
# ?????? ?????? 2
# 1
# ?????? ?????? 3
# 210
# ?????? ?????? 3
# 105
# ?????? ?????? 4
# 1000
# ?????? ?????? 4
# 144

# import sys
# data = int(sys.stdin.readline())
#
# count = 0
# # print(i)
# for check in range(1, data + 1):
#     temp_data = str(check)
#     if len(temp_data) == 4:
#         break
#     elif len(temp_data) <= 2:
#         count += 1
#     else:
#         temp_data = str(check)
#         if int(temp_data[0]) - int(temp_data[1]) == int(temp_data[1]) - int(temp_data[2]):
#             count+=1
#
# print(count)

# ??????
# ??????????????? ?????? ?????? ?????? ?????? ???????????? ????????? ????????? ??????. ????????? ?????? 21??? ?????? ?????? ?????? ?????????, ????????? ?????? ????????? ?????? ????????? ????????????. ???????????? ??????????????? ????????? ????????? ??????.
#
# ?????? ????????? ????????? ?????? ???????????? ????????? ????????? ????????? ????????? ??????, ???????????? ??????????????? ??????.
#
# ????????? ????????? ??????????????? ??? ???????????? ?????? ????????? ?????? ??????. ??? ??????, ????????? N?????? ????????? ?????? ????????? ???????????? ????????? ?????????. ?????? ?????? ????????? ?????? M??? ?????? ?????????.
#
# ?????? ??????????????? ????????? ?????? ?????? N?????? ?????? ????????? 3?????? ????????? ????????? ??????. ????????? ?????? ???????????? ?????????, ??????????????? ?????? ????????? ?????? M??? ?????? ???????????? M??? ????????? ????????? ???????????? ??????.
#
# N?????? ????????? ?????? ?????? ????????? ???????????? ???, M??? ?????? ???????????? M??? ????????? ????????? ?????? 3?????? ?????? ?????? ???????????????.
#
# ??????
# ?????? ?????? ????????? ?????? N(3 ??? N ??? 100)??? M(10 ??? M ??? 300,000)??? ????????????. ?????? ????????? ????????? ?????? ?????? ?????? ????????????, ??? ?????? 100,000??? ?????? ?????? ?????? ????????????.
#
# ?????? M??? ?????? ?????? ?????? 3?????? ?????? ??? ?????? ????????? ???????????? ????????????.
#
# ??????
# ?????? ?????? M??? ?????? ???????????? M??? ????????? ????????? ?????? 3?????? ?????? ????????????.

# ?????? ?????? 1
# 5 21
# 5 6 7 8 9
# ?????? ?????? 1
# 21
# ?????? ?????? 2
# 10 500
# 93 181 245 214 315 36 185 138 216 295
# ?????? ?????? 2
# 497

# import sys
# n, m = map(int,sys.stdin.readline().split())
#
# data = list(map(int, sys.stdin.readline().split()))
#
# # print(n,m)
# # print(data)
#
# result = []
# for i in range(n):
#     for j in range(0, i):
#         for k in range(i, n):
#             if i == j or i == k or j == k:
#                 continue
#             temp_result = data[i] + data[j] + data[k]
#             if temp_result == m:
#                 result.append(temp_result)
#                 break
#
#             if data[i] + data[j] + data[k] < m:
#                 result.append(data[i] + data[j] + data[k])
#
# print(max(result))

# ??????
# ?????? ????????? N??? ?????? ???, ??? ????????? N??? ???????????? N??? N??? ????????? ??? ???????????? ?????? ????????????.
# ?????? ????????? M??? ???????????? N??? ??????, M??? N??? ???????????? ??????. ?????? ??????, 245??? ???????????? 256(=245+2+4+5)??? ??????.
# ????????? 245??? 256??? ???????????? ??????. ??????, ?????? ???????????? ???????????? ???????????? ?????? ?????? ??????. ?????????, ???????????? ?????? ?????? ???????????? ?????? ??? ??????.
#
# ????????? N??? ???????????? ???, N??? ?????? ?????? ???????????? ???????????? ??????????????? ???????????????.
#
# ??????
# ?????? ?????? ????????? N(1 ??? N ??? 1,000,000)??? ????????????.
#
# ??????
# ?????? ?????? ?????? ????????????. ???????????? ?????? ???????????? 0??? ????????????.

# ?????? ?????? 1
# 216
# ?????? ?????? 1
# 198

# m = int(input())
#
# result = []
# for i in range(1, m+1):
#     temp = list(map(int, str(i)))
#     temp_result = i + sum(temp)
#     if temp_result == m:
#         print(i)
#
#     if i == m:
#         print(0)

head = [1,2,2,1]
# head = [1,2]
 # true
# Definition for singly-linked list.


import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

temp_head = ListNode(head[0])
for i in range(1,len(head)):
    temp_head.next = ListNode(head[i])
    temp_head = temp_head.next

print(temp_head)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # q = collections.deque()
        #
        # if not head:
        #     return True
        #
        # while head:
        #     q.append(head.val)
        #     head = head.next
        # # print(q)
        #
        # while len(q) > 1:
        #     if q.popleft() != q.pop():
        #         return False
        #
        # return True

        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev

print(Solution().isPalindrome(temp_head))