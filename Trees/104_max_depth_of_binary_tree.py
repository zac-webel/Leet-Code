# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints: 

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # treat any valid node as value = 1
        # run DFS recurively so when we backtrack we already have the left and right values 
        # left and right equal the height if that node was the root
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # always take the max height we have seen from this node and below
        return 1 + max(left,right)
        