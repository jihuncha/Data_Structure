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
#         # index 니까 -1 해줌
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
#                 # ??? 이전과의 차이만큼 물 높이 처리?
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
#             # 중복값 건너 뛰기
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
#                     # 같은 숫자만큼 이동
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



# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	68947	35835	30407	52.057%
# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# 예제 입력 1
# 110
# 예제 출력 1
# 99
# 예제 입력 2
# 1
# 예제 출력 2
# 1
# 예제 입력 3
# 210
# 예제 출력 3
# 105
# 예제 입력 4
# 1000
# 예제 출력 4
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

# 문제
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
#
# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
#
# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
#
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
#
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
#
# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
#
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
#
# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 예제 입력 1
# 5 21
# 5 6 7 8 9
# 예제 출력 1
# 21
# 예제 입력 2
# 10 500
# 93 181 245 214 315 36 185 138 216 295
# 예제 출력 2
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

# 문제
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다.
# 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
#
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
#
# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

# 예제 입력 1
# 216
# 예제 출력 1
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