"""
https://leetcode.com/problems/number-of-islands/

Approach:
Use DFS to replace "1" with 0 and each time dfs method is called increment the count. Return the count for number of islands.

Time Complexity: O(N*M)
Space Complexity: O(N*M)
"""

def num_island(matrix):
    if not matrix:
        return 0

    def dfs(i, j):
        matrix[i][j] = "0"
        if i>0 and matrix[i-1][j] == "1": dfs(i-1, j)
        if j>0 and matrix[i][j-1] == "1": dfs(i, j-1)
        if i<len(matrix)-1 and matrix[i+1][j] == "1": dfs(i+1, j)
        if j<len(matrix[0])-1 and matrix[i][j+1] == "1": dfs(i, j+1)

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "1":
                dfs(i,j)
                count+=1
    return count

matrix0 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

matrix1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

assert num_island(matrix0) == 1
assert num_island(matrix1) == 3