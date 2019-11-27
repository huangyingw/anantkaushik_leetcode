"""
Problem Link: https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
          return False
        m,n = len(matrix), len(matrix[0])
        low = 0
        high = (m * n) -1
        while low <= high:
          mid = (low+high)//2
          midElement = matrix[mid//n][mid%n]
          if midElement == target:
            return True
          elif midElement > target:
            high = mid -1
          else:
            low = mid + 1
        return False