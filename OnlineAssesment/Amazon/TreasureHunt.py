"""
https://leetcode.com/discuss/interview-question/347457

Approach:
Use BFS algorithm to explore space and do not explore space if it has been explored before. Maintain number of steps for each exploration and return the step count as soon as first treasure hunt is encountered. If treasure cannnot be reached safely return -1.

Time Complexity: O(N*M)
Space Complexity: O(N*M)
"""

def treasure_steps(matrix):
    if not matrix or matrix==[[]]:
        return -1

    queue = [(0,0)]
    step = 0
    visited = set()

    while queue:
        tmp = []

        for i,j in queue:
            visited.add((i,j))
            if matrix[i][j] == "X":
                return step
            elif i>0 and (i-1,j) not in visited and matrix[i-1][j] != "D":
                tmp.append((i-1,j))
            elif j>0 and (i,j-1) not in visited and matrix[i][j-1] != "D":
                tmp.append((i,j-1))
            elif i<len(matrix)-1 and (i+1,j) not in visited and matrix[i+1][j] != "D":
                tmp.append((i+1,j))
            elif j<len(matrix[0])-1 and (i,j+1) not in visited and matrix[i][j+1] != "D":
                tmp.append((i,j+1))
        queue = tmp
        step+=1

    return -1

mat1 = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

assert(treasure_steps(mat1)) == 5