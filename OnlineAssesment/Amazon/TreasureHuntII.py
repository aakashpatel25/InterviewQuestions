"""
https://leetcode.com/discuss/interview-question/356150

Approach:
Run BFS N times to get answer for each starting point and return the minimum of the starting point.

Time Complexity: O(N*M)
Space Complexity; O(N*M)
"""
import sys

def bfs(sp, matrix):
    queue = sp
    step = 0
    visited = set()

    while queue:
        tmp = []

        for i, j in queue:
            visited.add((i,j))
            if matrix[i][j] == "X":
                return step

            if i>0 and (i-1,j) not in visited and matrix[i-1][j] != "D":
                tmp.append((i-1, j))

            if j>0 and (i,j-1) not in visited and matrix[i][j-1] != "D":
                tmp.append((i, j-1))

            if i < len(matrix)-1 and (i+1,j) not in visited and matrix[i+1][j] != "D":
                tmp.append((i+1,j))

            if j < len(matrix[0])-1 and (i,j+1) not in visited and matrix[i][j+1] != "D":
                tmp.append((i,j+1))

        queue = tmp
        step +=1

    return sys.maxsize


def get_min_dist(matrix):
    # dist = []

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == "S":
    #             dist.append(bfs((i,j), matrix))

    # if not dist or min(dist) == sys.maxsize:
    #     return -1
    # else:
    #     return min(dist)
    sp = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                sp.append((i,j))

    return bfs(sp, matrix)

matrix = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]


assert get_min_dist(matrix) == 3