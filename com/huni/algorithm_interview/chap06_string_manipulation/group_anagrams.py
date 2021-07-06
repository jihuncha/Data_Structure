# https://leetcode.com/problems/group-anagrams/

# 그룹 에너그램


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example1:
#
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
#
# Example2:
#
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for check_all in strs:
            # print(collections.Counter(check_all))
            # print(''.join(sorted(check_all)))
            temp = ''.join(sorted(check_all))
            if temp not in dic:
                dic[temp] = [check_all]
            else:
                dic[temp].append(check_all)

        return list(dic.values())

        # for check_all in strs:
        #     temp_list = list(set(check_all))
        #     temp_list.sort()
        #     # print(temp_list)
        #     str_temp = ''
        #     for i in temp_list:
        #         str_temp += i
        #     # print(str_temp)
        #     if str_temp not in dic:
        #         dic[str_temp] = [check_all]
        #     else:
        #         dic[str_temp].append(check_all)
        # # print(dic)
        # return sorted(list(dic.values()))



print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams(["ddddddddddg","dgggggggggg"]))