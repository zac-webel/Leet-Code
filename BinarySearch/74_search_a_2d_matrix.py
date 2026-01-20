# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])

        # run binary search on rows to find which row it would be

        top_r = 0
        bottom_r = n_row - 1

        while top_r<=bottom_r:
            mid_r = top_r + (bottom_r-top_r) // 2
            if matrix[mid_r][0]==target:
                return True
            if matrix[mid_r][0]<target:
                top_r = mid_r + 1
            else:
                bottom_r = mid_r -1

        # run binary search on the chosen rows columns to find which col it would be
        left = 0
        right = n_col - 1
        while left<=right:
            mid = left + (right - left) // 2
            if matrix[bottom_r][mid] == target:
                return True
            if matrix[bottom_r][mid]<target:
                left = mid+1
            else:
                right = mid - 1
        
        return False
