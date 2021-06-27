# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# 이진 트리 깊이

import collections

# root = [3, 9, 20, None, None, 15, 7]
# Output: 3
# Example
# 2:
#
# Input: root = [1, null, 2]
# Output: 2
# Example
# 3:
#
# Input: root = []
# Output: 0
# Example
# 4:
#
# Input: root = [0]
# Output: 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


array = [3, 9, 20, None, None, 15, 7]
root = TreeNode(array[0])
tree_array = [root]

for i in range(len(array)):
    if array[i]:
        if i * 2 + 1 < len(array) and array[i * 2 + 1]:
            left_node = TreeNode(array[i * 2 + 1])
            tree_array[i].left = left_node
            tree_array.append(left_node)
        if i * 2 + 1 < len(array) and array[i * 2 + 2]:
            right_node = TreeNode(array[i * 2 + 2])
            tree_array[i].right = right_node
            tree_array.append(right_node)

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#
#         queue = collections.deque([root])
#         depth = 0
#
#         while queue:
#             depth += 1
#
#             for _ in range(len(queue)):
#                 cur_root = queue.popleft()
#                 if cur_root.left:
#                     queue.append(cur_root.left)
#                 else:
#                     queue.append(cur_root.right)
#         return depth

        # print(root)


    # def bfs(self, check: TreeNode, count:int) -> int:


from collections import deque


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return depth


print(Solution().max_depth(root))