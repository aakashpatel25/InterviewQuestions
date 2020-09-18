"""
https://leetcode.com/discuss/interview-question/349617

Approach:
Use recursion to compute average for earch node that are not leaf and return the node with maximum value.

For optimization use dfs algorithm and compute average as you go and return the node.


Time Complexity: O(N)
Space Complexity: O(N)
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = []

def preroder(root):
    if not root:
        return []
    res = [root.val]
    for ele in root.child:
        res+=preroder(ele)
    return res

# def get_maximum_average_subtree(root):
#     max_avg = 0
#     max_root = root.val

#     def explore(root, max_avg, max_root):
#         if not root or not root.child:
#             return max_avg, max_root
#         total = preroder(root)
#         if sum(total)/len(total) > max_avg:
#             max_avg = max(sum(total)/len(total), max_avg)
#             max_root = root.val
#         for ele in root.child:
#             explore(ele, max_avg, max_root)
#         return max_avg, max_root

#     return explore(root,max_avg,max_root)


def dfs(root, total, max_val, max_root_val, count):
    if not root.child:
        return root.val, 1, max_val, max_root_val

    total_val, total_count = root.val, 1
    for child in root.child:
        cur_sum, cur_count, max_val, max_root_val = dfs(child, total_val, max_val, max_root_val, total_count)
        total_val+=cur_sum
        total_count+=cur_count

    if total_val/total_count > max_val:
        max_val = total_val/total_count
        max_root_val = root.val

    return total_val, total_count, max_val, max_root_val

def optimal_solution(root):
    if not root: return None
    return dfs(root, 0, 0, root.val, 0)[3]

# 	 20
# 	   /   \
# 	 12     18
#   /  |  \   / \
# 11   2   3 15  8
root = TreeNode(20)
root.child.append(TreeNode(12))
root.child.append(TreeNode(18))
root.child[0].child.append(TreeNode(11))
root.child[0].child.append(TreeNode(2))
root.child[0].child.append(TreeNode(3))
root.child[1].child.append(TreeNode(15))
root.child[1].child.append(TreeNode(8))

assert optimal_solution(root) == 18