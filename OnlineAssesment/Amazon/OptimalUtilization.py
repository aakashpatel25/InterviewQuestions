"""
https://leetcode.com/discuss/interview-question/373202

Approach:
Naive just multiply all the numbers and get the one with the closest to the tagert.

Time: O(N*M)
Space: O(N+M)
"""

def get_optimal_utilization(a,b,target):
    res = []
    a.sort(key=lambda item: item[1])
    b.sort(key=lambda item: item[1])

    for a_id, a_val in a:
        if a_val > target:
            break

        for b_id, b_val in b:
            cur_sum = a_val + b_val
            if cur_sum <= target:
                if not res or res and res[0][2] < cur_sum:
                    res = [[a_id, b_id, cur_sum]]
                elif res[0][2] == cur_sum:
                    res.append([a_id, b_id, cur_sum])
            else:
                break

    return [[a_id, b_id] for a_id, b_id, _ in res]


a1 = [[1, 2], [2, 4], [3, 6]]
b1 = [[1, 2]]

a2 = [[1, 3], [2, 5], [3, 7], [4, 10]]
b2 = [[1, 2], [2, 3], [3, 4], [4, 5]]

a3 = [[1, 8], [2, 7], [3, 14]]
b3 = [[1, 5], [2, 10], [3, 14]]

a4 = [[1, 8], [2, 15], [3, 9]]
b4 = [[1, 8], [2, 11], [3, 12]]

assert get_optimal_utilization(a1,b1, 7) == [[2, 1]]
assert get_optimal_utilization(a2, b2, 10) == [[2, 4], [3, 2]]
assert get_optimal_utilization(a3, b3, 20) == [[3, 1]]
assert get_optimal_utilization(a4, b4, 20) == [[1, 3], [3, 2]]
assert get_optimal_utilization(a1,b1, 0) == []