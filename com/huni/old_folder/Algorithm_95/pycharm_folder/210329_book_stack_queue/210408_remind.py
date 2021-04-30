# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

# Example 4:
#
# s = "([)]"
# Output: false
# Example 5:
#
# Input: s = "{[]}"
# Output: true

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:
#
from typing import List

s = "ebcabc"
# Output: "abc"
#
# Example 2:
s = "cbacdcbc"
# Output: "acdb"

T = [73, 74, 75, 71, 69, 72, 76, 73]
#
# [1, 1, 4, 2, 1, 1, 0, 0].

height = [0,1,0,2,1,0,1,3,2,1,2,1]

import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(',
               '}':'{',
               ']':'[' }

        if len(s) == 0:
            return True

        for char in s:
            print(char)
            if char not in dic:
                print("append")
                stack.append(char)
            elif not stack or dic[char] != stack.pop():
                print("{} - {}".format(stack, dic[char]))
                return False

        return len(stack) == 0

    def removeDuplicateLetters(self, s: str) -> str:
        # for char in sorted(set(s)):
        #     suffix = s[s.index(char):]
        #
        #     print(suffix)
        #     if set(s) == set(suffix):
        #         print(set(s))
        #         return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        # return ''

        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            print(char)
            counter[char] -= 1
            if char in stack:
                print("continue")
                continue
            # 이전보다 앞선 문자이고, 뒤에 다시 붙일 문자가 남아있는 경우
            if stack:
                print("stack : ", stack)
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
                # stack.pop()
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result, stack = [0] * len(T), []

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)

        return result

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_height, right_height = height[left], height[right]
        count = 0

        while left < right:
            if left_height < right_height:
                left += 1
                if left_height - height[left] > 0:
                    count += left_height - height[left]
                left_height = max(left_height, height[left])
            else:
                right -=1
                if right_height - height[right] > 0:
                    count += right_height - height[right]
                right_height = max(right_height, height[right])

        return count


# print(Solution().trap(height))
# print(Solution().dailyTemperatures(T))

# class Solution:


import collections

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q(0)

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0

    def check(self) -> List:
        return self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

q = MyStack()
q.push(1)
q.push(2)
q.push(3)
print(q.check())