# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


# Input: s = "bcabc"
# Output: "abc"

# Input: s = "cbacdcbc"
# Output: "acdb"

# s = "bcabc"
import collections

s = "cbacdcbc"
class Solution:
    # def removeDuplicateLetters(self, s: str) -> str:
    #     for char in sorted(set(s)):
    #         print("char - {}".format(char))
    #         suffix = s[s.index(char):]
    #         print("suffix - {}".format(suffix))
    #
    #         if set(s) == set(suffix):
    #             print("set(s) == set(suffix)")
    #             return char + self.removeDuplicateLetters(suffix.replace(char, ''))
    #
    #     return ''

    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        print(counter)

        for char in s:
            counter[char] -= 1
            print('counter - {}'.format(counter))
            if char in seen:
                print('continue')
                continue

            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                print("stack/counter - {},{}".format(stack[-1], counter[stack[-1]]))
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)

print(Solution().removeDuplicateLetters(s))





