"""
https://leetcode.com/discuss/interview-question/793606/

Approach: Compute the number of units for each box sort it in descending order and fill up the truck till it is full.

Time Complexity: O(MlogM) - Sorting would require this complexity
Space Complexity: O(M) - Where M sum(boxes)
"""

def get_max_unit(num, boxes, unit_size, units_per_box, truck_size):
    units = []

    for boxes, unit in zip(boxes, units_per_box):
        units+= [unit]*boxes

    units.sort(reverse=True)
    return sum(units[:truck_size])

assert get_max_unit(3, [1,2,3], 3, [3,2,1], 3) == 7
assert get_max_unit(3, [2,5,3], 3, [3,2,1], 50) == 19