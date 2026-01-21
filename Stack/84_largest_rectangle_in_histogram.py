# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # idx, height
        ans = 0
        
        for idx, h in enumerate(heights):
            starting_pos = idx
            while stack and h<stack[-1][1]:
                idx_p, h_p = stack.pop()
                width = idx-idx_p 
                ans = max(ans, h_p*width)
                starting_pos = idx_p
            stack.append((starting_pos,h))

        while stack:
            idx_p, h_p = stack.pop()
            height = h_p
            width = (n) - idx_p 
            ans = max(ans, height*width)
        return ans
