# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
from typing import List

# from collections import Counter
# import re
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         change_str = []
#         # for delete_str in str:
#         #     print(delete_str)
#         print(paragraph)
#         for check in banned:
#             if check in paragraph:
#                 paragraph = paragraph.replace(check, "")
#         print(paragraph)
#
#         list_str = paragraph.lower().split()
#         print(list_str)
#         print(Counter(list_str).most_common(1))
#
# print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
# print(Solution().mostCommonWord("a.", []))

##############
# 쉼표 구두점등의 전처리 과정이 필요한데 그걸 모르겟음
# 결국 re를 사용해야한다.

### 풀이
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#sample
# ^ -> now
# \w 문자
# 문자가 아닌것은 모두 공백으로 치환
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()]
print(words)

# 정렬한 값을 키로 dict 에 추가한다. 존재하지않는 키를 삽입하면 keyerror가 뜨기 떄문에 defaultdict으로 한다.

import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(Solution().mostCommonWord("a.", []))