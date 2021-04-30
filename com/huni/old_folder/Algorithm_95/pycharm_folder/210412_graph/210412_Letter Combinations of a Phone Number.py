from typing import List

digits = "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# digits = ""
# Output: []
#
# digits = "2"
# Output: ["a", "b", "c"]


import collections
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # mapping = {
        #     '1': [],
        #     '2': ['a','b','c'],
        #     '3': ['d', 'e', 'f'],
        #     '4': ['g', 'h', 'i'],
        #     '5': ['j', 'k', 'l'],
        #     '6': ['m', 'n', 'o'],
        #     '7': ['p', 'q', 'r', 's'],
        #     '8': ['t', 'u', 'v'],
        #     '9': ['w', 'x', 'y', 'z'],
        #     '10': [],
        # }
        #
        # queue = collections.deque()
        # print(type(queue))
        # result = []
        # def dfs(input_num: str) -> List:
        #     for idx,str_check in enumerate(input_num):
        #         if not mapping[str_check]:
        #             continue
        #         if not result:
        #             print("test")
        #             for test in mapping[str_check]:
        #                 result.append(test)
        #         else:
        #             for j in range(len(mapping[str_check])):
        #                 if not result[j]:
        #                     result.append(mapping[str_check][j])
        #                 else:
        #                     print(result[j])
        #                     result[j] = result[j] + mapping[str_check][j]
        #
        # dfs(digits)
        # print(result)

        def dfs(index, path):
            print(path)
            # 끝까지 탐색하면 백트래킬
            if len(path) == len(digits):
                result.append(path)
                return

            #입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    print("digits - {}, and j - {}".format(digits[i], j))
                    dfs(i + 1, path + j)


        if not digits:
            return []
        dic = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        dfs(0,"")

        return result


print(Solution().letterCombinations(digits))


#백트래킹
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         # If the input is empty, immediately return an empty answer array
#         if len(digits) == 0:
#             return []
#
#         # Map all the digits to their corresponding letters
#         letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
#                    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#
#         def backtrack(index, path):
#             # If the path is the same length as digits, we have a complete combination
#             if len(path) == len(digits):
#                 combinations.append("".join(path))
#                 return  # Backtrack
#
#             # Get the letters that the current digit maps to, and loop through them
#             possible_letters = letters[digits[index]]
#             for letter in possible_letters:
#                 # Add the letter to our current path
#                 path.append(letter)
#                 # Move on to the next digit
#                 backtrack(index + 1, path)
#                 # Backtrack by removing the letter before moving onto the next
#                 path.pop()
#
#         # Initiate backtracking with an empty path and starting index of 0
#         combinations = []
#         backtrack(0, [])
#         return combinations