# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]
from typing import List
import collections

strs = ["eat","tea","tan","ate","nat","bat"]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # str_dict = collections.defaultdict(list)
        dic_sample = {}

        for words in strs:
            temp = ''.join(sorted(words))
            if temp not in dic_sample:
                dic_sample[temp] = [words]
            else:
                dic_sample[temp].append(words)

        print(list(dic_sample.values()))
        return list(dic_sample.values())


print(Solution().groupAnagrams(strs))
# str_test = "abc"
# str_test_second = "bac"
#
# sam = [word for word in str_test]
# print(sam)
# print(sorted(str_test_second))
# print(sorted(str_test_second) == sam)
# # print(str_test.)


### 풀이
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())