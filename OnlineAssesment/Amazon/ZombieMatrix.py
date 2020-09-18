"""
https://leetcode.com/discuss/interview-question/411357/

Approach:
Get initial starting points. Use BFS to go though each of the starting points. And return the maximum number of levels required to convert entire matrix to 1s.

Time Complexity: O(N*M)
Space Complexity: O(N*M)


Related Question: Rotten Oranges - https://leetcode.com/submissions/detail/378545773/
"""

def zombine_matrix(matrix):
    if not matrix: return -1
    sp, level = [], 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]: sp.append((i,j))

    if not sp: return -1

    while sp:
        tmp = []
        for (i,j) in sp:
            if i>0 and matrix[i-1][j] == 0:
                matrix[i-1][j] = 1
                tmp.append((i-1, j))

            if j>0 and matrix[i][j-1] == 0:
                matrix[i][j-1] = 1
                tmp.append((i, j-1))

            if i<len(matrix)-1 and matrix[i+1][j] == 0:
                matrix[i+1][j] = 1
                tmp.append((i+1, j))

            if j<len(matrix[0])-1 and matrix[i][j+1] == 0:
                matrix[i][j+1] = 1
                tmp.append((i, j+1))

        sp = tmp
        if sp:
            level+=1


    return level

print(zombine_matrix([[0, 1, 1, 0, 1],[0, 1, 0, 1, 0],[0, 0, 0, 0, 1],[0, 1, 0, 0, 0]]))