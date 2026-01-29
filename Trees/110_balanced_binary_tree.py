# Given a binary tree, determine if it is height-balanced.

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Initialize answer to true
        balanced = [True]
        
        def height(node):
            # base case child is null 
            if not node: return 0
            
            # get left height + early exit
            left = height(node.left)
            if balanced[0] == False: return 0

            # get right height 
            right = height(node.right)

            # if any any point we are not balanced, early exit
            if abs(left-right)>1: 
                balanced[0] = False
                return 0
            
            # return the height
            return 1 + max(left, right)
        
        # call function
        height(root)

        return balanced[0]