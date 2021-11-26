# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


root = [1,2,3,None,None,4,5]

# Output: [1,2,3,None,None,4,5]

root = []

# Output: []

root = [1]

# Output: [1]

root = [1,2]

# Output: [1,2]

# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# tree 생성로직
array = [1,2,3,None,None,4,5]
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

###############################################################################################
from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        result = ['#']
        while queue:
            temp = queue.popleft()

            if temp:
                queue.append(temp.left)
                queue.append(temp.right)

                # print(temp.val)
                result.append(str(temp.val))
            else:
                # print("None")
                result.append('#')

        # 1. list to String
        # 2. 양쪽끝의 #제거 
        # 3. replace # -> ''
        result = ''.join(result).strip("#").replace('#','')

        return result


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        print(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

print(Codec().serialize(root1))