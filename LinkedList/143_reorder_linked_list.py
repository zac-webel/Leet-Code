# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle by moving slow 1/2 the speed of fast 
        # when fast is at the end of the list, slow is 1/2 the way through
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse right side of list
        curr, prev = slow, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # merge by alternating from each linked list 
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

