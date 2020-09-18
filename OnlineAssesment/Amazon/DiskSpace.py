"""
https://leetcode.com/discuss/interview-question/808348/

Approach:
Idea is to use fix sliding window apporach. For each sliding window, mantain minimum and recompute it if min element is removed when sliding the window over by 1 element, else min would be min(curMin, curElement). For each sliding window we would set max to be of max(maximum, curMin) to get maximum minimum segment space available over all computer. Here is an implementation in python.

Time Complexity: O(N*K) (Where K is the size of the segment) - This would happend when we would need to recompute min each time we slide window over

Space Complexity: O(1)
"""
import sys

def max_min_segment_space(num_comp, space_list, size):
    maximum = 0
    cur_min = sys.maxsize

    for i, space in enumerate(space_list):
        if i<size:
            cur_min = min(cur_min, space)
        else:
            maximum = max(maximum, cur_min)

            if space_list[i-size] == cur_min:
                cur_min = min(space_list[i-size+1:i+1])
            else:
                cur_min = min(cur_min, space)

    # For last sliding window we need this comparation
    maximum = max(maximum, cur_min)
    return maximum

assert max_min_segment_space(6, [8,4,2,6,9,7], 3) == 6
assert max_min_segment_space(6, [8,4,2,6,9,7], 2) == 7
assert max_min_segment_space(6, [8,4,2,6,9,7], 1) == 9
assert max_min_segment_space(6, [8,4,2,6,9,7], 4) == 2
assert max_min_segment_space(3, [8,2,4], 2) == 2
assert max_min_segment_space(3, [8,2,4], 1) == 8