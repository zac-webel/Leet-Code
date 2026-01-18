# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# two pointer
# out to in 
# store the max height left and right
# stored water = max height left - height[left] or max height right - height[right]

# O(n) and O(1) space

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        high_left, high_right = height[left], height[right]
        ans = 0

        while left<right:
            if high_left<high_right:
                ans += high_left - height[left]
                left+=1
                high_left = max(high_left,height[left])
            else:
                ans += high_right - height[right]
                right-=1
                high_right = max(high_right,height[right])

        return ans