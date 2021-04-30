# https://leetcode.com/problems/reorder-data-in-log-files/

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digits = [], []

        for i in logs:
            # print(i.split()[1].isdigit())
            # if i.split(1)
            if i.split()[1].isdigit():
                digits.append(i)
            else:
                letter.append(i)
        print(letter)
        print(digits)

        letter.sort(key=lambda x:[x.split()[1:], x.split()[0]])

        return letter + digits



logs_temp = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solution().reorderLogFiles(logs_temp))

