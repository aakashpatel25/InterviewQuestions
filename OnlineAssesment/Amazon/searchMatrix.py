"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Approach:
Objective here is to be able to search target element in matrix of elements that are sorted row wise and column sise.

One approach could be to do binary search on each row where start<target<end else return False

It could be further optmized to move i and j around the matrix heuristically to get closer to the element.

Time Complexity: O(J+I)
Space Complexity: O(1)
"""

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix: return False
    i, j = 0, len(matrix[0])-1

    while i<len(matrix) and j>=0:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            j-=1
        else:
            i+=1

    return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
assert searchMatrix(matrix, 5) == True
assert searchMatrix(matrix, 1) == True
assert searchMatrix(matrix, 7) == True
assert searchMatrix(matrix, 16) == True
assert searchMatrix(matrix, 30) == True
assert searchMatrix(matrix, 20) == False
assert searchMatrix(matrix, 50) == False
assert searchMatrix(matrix, 111) == False
assert searchMatrix(matrix, 0) == False