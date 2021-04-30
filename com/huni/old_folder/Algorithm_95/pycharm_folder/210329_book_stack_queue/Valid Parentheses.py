# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Input: s = "()"
# Output: true
#
# Input: s = "()[]{}"
# Output: true
#
# Input: s = "(]"
# Output: false

# Input: s = "([)]"
# Output: false
#
# Input: s = "{[]}"
# Output: true
from typing import List
s = "()[]{}"

class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        table = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            print("char - {}".format(char))
            if char not in table:
                print('append')
                q.append(char)
            elif not q or table[char] != q.pop():
                print('false')
                return False
            else:
                print('check {} '.format(table[char]))
        return len(q) == 0

print(Solution().isValid(s))