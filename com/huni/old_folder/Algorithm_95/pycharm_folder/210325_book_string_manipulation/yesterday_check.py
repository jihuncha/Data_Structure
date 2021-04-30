from collections import deque


# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# palindrome
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         check = deque()
#         for char in s:
#             if char.isalnum():
#                 check.append(char.lower())
#
#         while len(check) > 1:
#             if check.popleft() != check.pop():
#                 return False
#         return True
#
# print(Solution().isPalindrome("race a car"))

#reverse String

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List
#
#
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s.reverse()
#둘중 하나 선택!
#         s[:] = s[::-1]
#         return s
#         # return s[::-1]
#
# print(Solution().reverseString(s))

#Reorder Data in Log Files

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digits = [], []
        for make_list in logs:
            # print(make_list[1:])
            if make_list.split()[1].isdigit():
                digits.append(make_list)
            else:
                letter.append(make_list)

        letter.sort(key=lambda x: [x.split()[1:], x.split()[0]])
        return letter + digits

print(Solution().reorderLogFiles(logs))