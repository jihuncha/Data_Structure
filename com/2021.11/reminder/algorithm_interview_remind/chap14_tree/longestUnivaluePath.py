# https://leetcode.com/problems/longest-univalue-path/

# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value.
#
# This path may or may not pass through the root.
#
# The length of the path between two nodes is represented by the number of edges between them.
from typing import Optional

root = [5,4,5,1,1,5]

# Output: 2

root = [1,4,5,4,4,5]

# Output: 2

# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# tree 생성로직
array =  [1,4,5,4,4,5]
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node:TreeNode):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            return max(left, right) + 1

        return 0


print(Solution().longestUnivaluePath(root))
