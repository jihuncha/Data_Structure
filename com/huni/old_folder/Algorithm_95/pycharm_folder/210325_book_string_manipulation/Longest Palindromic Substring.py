# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"

# Input: s = "a"
# Output: "a"

# Input: s = "ac"
# Output: "a"

########## 잘 이해가 안감..
temp_s = "babad"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''

        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)

        return result

print(Solution().longestPalindrome(temp_s))

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         m = ''  # Memory to remember a palindrome
#         for i in range(len(s)):  # i = start, O = n
#             for j in range(len(s), i, -1):  # j = end, O = n^2
#                 if len(m) >= j-i:  # To reduce time
#                     break
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m

# leetcode 예시
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         m = ''  # Memory to remember a palindrome
#         for i in range(len(s)):  # i = start, O = n
#             for j in range(len(s), i, -1):  # j = end, O = n^2
#                 if len(m) >= j-i:  # To reduce time
#                     break
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m