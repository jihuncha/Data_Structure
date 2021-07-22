# https://leetcode.com/problems/longest-palindromic-substring/

# 가장 긴 팰랜드롬

# Example 1:
#
s = "babad"
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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''

        def expand(left:int, right:int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s[:] == s[::-1]:
            return s

        for i in range(len(s) - 1):
            result = max(result, expand(i, i +1), expand(i, i+2), key = len)

        return result

print(Solution().longestPalindrome(s))