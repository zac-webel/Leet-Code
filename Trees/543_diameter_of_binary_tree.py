# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # initalize anser to be 0
        ans = [0]

        def height(node):
            if not node: return 0

            # DFS 
            left = height(node.left)
            right = height(node.right)

            # ans = max of ans and the number of edges = right + left
            ans[0] = max(ans[0], right+left)

            # return the height
            return 1 + max(left,right)
        
        height(root)
        return ans[0]

        

