# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        cpy = head
        while cpy:
            len_list+=1
            cpy = cpy.next
        
        idx_to_remove = len_list - n
        dummy = ListNode()
        start = dummy
        cur_idx = 0
        while head:
            if idx_to_remove!=cur_idx:
                start.next = ListNode(val = head.val)
                start = start.next
            head = head.next
            cur_idx+=1
        return dummy.next