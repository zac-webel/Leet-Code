# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Input: p = [1,2], q = [1,null,2]
# Output: false

from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(p,q):
            # If both NULL that is accepted
            if not p and not q: return True

            # if one is NULL and one is not, fail
            if (not p and q) or (p and not q): return False

            # If the values don't match, fail
            if p.val!=q.val: return False

            # Call recursion 
            return same(p.left, q.left) and same(p.right, q.right)
        
        return same(p,q)