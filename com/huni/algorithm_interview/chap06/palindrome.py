# https://leetcode.com/problems/valid-palindrome/

# 팰린드롬 = 회문
# 거꾸로 읽어도 똑같은

s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
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

print(Solution().isPalindrome(s))



