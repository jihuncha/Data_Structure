# https://leetcode.com/problems/merge-two-binary-trees/

# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
from typing import Optional

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]

# Output: [3,4,5,5,4,null,7]

root1 = [1]
root2 = [1,2]

# Output: [2,2]

# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# tree 생성로직
array = [1,3,2,5]
root1 = TreeNode(array[0])
tree_array = [root1]

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

array = [2,1,3,None,4,None,7]
root2 = TreeNode(array[0])
tree_array = [root2]

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


from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        root1_list = deque([root1])
        root2_list = deque([root2])

        while root1_list or root2_list:
            temp_1 = root1_list.popleft()
            temp_2 = root2_list.popleft()

            if temp_1.left and temp_2.left:
                temp_1.left.val = temp_1.left.val + temp_2.left.val
            root1_list.append(temp_1.left)
            root2_list.append(temp_2.left)

            if temp_1.right and temp_2.right:
                temp_1.right.val = temp_1.right.val + temp_2.right.val
            root1_list.append(temp_1.right)
            root2_list.append(temp_2.right)

        return root1

print(Solution().mergeTrees(root1,root2))