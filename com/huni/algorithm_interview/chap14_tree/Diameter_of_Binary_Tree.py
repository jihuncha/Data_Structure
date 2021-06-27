# https://leetcode.com/problems/diameter-of-binary-tree/

# 이진 트리 직경
from typing import List

root = [1,2,3,4,5]
# Output: 3
# Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].

# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

array = [1,2,3,4,5]
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


#### 이해가 안가네 ㅠㅠ 다시봐야할듯
# 상태값 : 리프 노드에서 현재 노드 까지의 거리
#
class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            # count+=1
            left = dfs(node.left)
            right = dfs(node.right)

            # print("left - ", left, " and count - ", count)
            # print("right - ", right, " and count - ", count)

            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest

print(Solution().diameterOfBinaryTree(root))

