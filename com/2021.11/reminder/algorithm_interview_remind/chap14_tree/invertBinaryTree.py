# https://leetcode.com/problems/invert-binary-tree/

# Given the root of a binary tree, invert the tree, and return its root.
from typing import Optional

root = [4,2,7,1,3,6,9]

# Output: [4,7,2,9,6,3,1]

root = [2,1,3]
# Output: [2,3,1]

root = []
# Output: []

# Constraint
#
# s:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tree 생성로직
array = [4,2,7,1,3,6,9]
root = TreeNode(array[0])
tree_array = [root]

if len(array) >= 3:
    for i in range(len(array)):
        if array[i] and i * 2 + 2 < len(array):
            if i * 2 + 1 < len(array) and array[i * 2 + 1]:
                left_node = TreeNode(array[i * 2 + 1])
                tree_array[i].left = left_node
                tree_array.append(left_node)
            if i * 2 + 1 < len(array) and array[i * 2 + 2]:
                right_node = TreeNode(array[i * 2 + 2])
                tree_array[i].right = right_node
                tree_array.append(right_node)
elif len(array) == 2:
    if array[1]:
        left_node = TreeNode(array[1])
        tree_array[0].left = left_node
        tree_array.append(left_node)


class Solution:
    result_tree:TreeNode

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node:TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            # print(left)
            right = dfs(node.right)

            left, right = right, left

            return max(left, right) + 1

        dfs(root)
        return root

print(Solution().invertTree(root))
