# https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.

from typing import Optional

root = [1, 2, 3, 4, 5]

# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

root = [1, 2]


# Output: 1

# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tree 생성로직
array = [1, 2, 3, 4, 5]
root = TreeNode(array[0])
tree_array = [root]

if len(array) >= 3:
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
elif len(array) == 2:
    if array[1]:
        left_node = TreeNode(array[1])
        tree_array[0].left = left_node
        tree_array.append(left_node)

from collections import deque


class Solution:
    longest_time = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            # print(node.val, node.left.val, node.right.val)

            if not node:
                # print("Test")
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            # Longest 값
            self.longest_time = max(self.longest_time, left + right + 2)

            # 상태값
            return max(left, right)

        dfs(root)

        return self.longest_time


print(Solution().diameterOfBinaryTree(root))

## 해결방법을 잘모르겠음
# 가장 말단 - 리프 노드까지 탐색하여 다음 부모로 거슬러 올라가면서 가각의 거리를 계산해 상태값을 업데이트하면서 누적
# 존재하지 않는 노드에 -1의 값을 부여 -> 거슬러 올라가면서 체크
# dfs
