# https://leetcode.com/problems/valid-palindrome/

# 팰린드롬 = 회문
# 거꾸로 읽어도 똑같은

#리스트 변환처리
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#
#         for char in s:
#             # 숫자와 영어만 인지
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#
#         return True

#deque 이용하여 속도 개선
from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strs = []

        strs = deque()
        # strs: Deque = collections.deque()

        for char in s:
            # 숫자와 영어만 인지
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

# 슬라이싱
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))






