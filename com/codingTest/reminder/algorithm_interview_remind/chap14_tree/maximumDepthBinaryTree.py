# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# import null
root = [3,9,20,None,None,15,7]
# Output: 3

# root = [1,null,2]
# Output: 2

# root = []
# Output: 0

# root = [0]

# Output: 1

# Definition for a binary tree node.
import collections

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# tree 생성로직
array =  [1,None,2]
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

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0

        queue = collections.deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return depth

print(Solution().maxDepth(root))