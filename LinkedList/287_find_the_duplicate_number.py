# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the cycle
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # move until the cycle is repeated
        p1 = nums[0]
        p2 = slow
        while p1!=p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1