# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List



digits = "23"

# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


# digits = ""

# Output: []


# digits = "2"

# Output: ["a","b","c"]


# 반례에 왜 01이 들어가..ㅋㅋ 문제조건이랑 다름
# digits = "0123456789"


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result_list = []

        dic = {
            "0" : [],
            "1" : [],
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        def dfs(input_num:str, append_list:str):
            if len(input_num) == 0:
                if len(append_list) != 0:
                    result_list.append(append_list)
                return

            temp, left_num = str(input_num[0]), str(input_num[1:])

            # 이거 문제 조건이랑 다른데?
            if len(dic[temp]) == 0:
                dfs(left_num, append_list)
                return

            for x in dic[temp]:
                dfs(left_num, append_list + x)

        dfs(digits, "")

        return result_list

print(Solution().letterCombinations(digits))

########풀이코드

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         def dfs(index, path):
#             # 끝까지 탐색하면 백트래킹
#             if len(path) == len(digits):
#                 result.append(path)
#                 return
#
#             # 입력값 자릿수 단위 반복
#             for i in range(index, len(digits)):
#                 # 숫자에 해당하는 모든 문자열 반복
#                 for j in dic[digits[i]]:
#                     dfs(i + 1, path + j)
#
#         # 예외 처리
#         if not digits:
#             return []
#
#         dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
#                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#         result = []
#         dfs(0, "")
#
#         return result