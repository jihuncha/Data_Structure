# https://leetcode.com/problems/reverse-string/solution/

from typing import List

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#
#         temp_list = []
#         for i in range(len(s)):
#             temp_list.append(s[i])
#         # index
#         left, right = 0, len(temp_list) - 1
#         while left < right:
#             temp_list[left], temp_list[right] = temp_list[right], temp_list[left]
#             left += 1
#             right -= 1
#
#         print(temp_list)
# print(Solution().reverseString("hello"))

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # return s[::-1]
        # 풀이 1
        s.reverse()
        # 풀이 2
        # 공간복잡도 제약에 의해 하기와같이 표현해야 사용가능
        s[:] = s[::-1]

print(Solution().reverseString("hello"))

# temp_list = [1,2,3]
# second_list = [4,5,6]
#
# for check in range(3):
#     temp_list[check],  second_list[check] = second_list[check], temp_list[check]
#
# print(temp_list, second_list)