"""
https://leetcode.com/discuss/interview-question/356960

Approach:
Use dictionary to determine indexes of each number. Keep track of max. If current number is greater than max and target-num is in dict there is a more suitable pair. Dictionary lookup would be O(1) so this problem can be solved in O(N)

Time Complexity: O(N)
Space Complexity: O(N)
"""
import collections
import sys

def find_pair_given_sum(nums, target):
    target-=30

    pair = []
    data = collections.defaultdict(list)

    for i, num in enumerate(nums):
        data[num].append(i)


    cmax = -sys.maxsize
    for num in nums:
        if target-num in data and num > cmax:
            if num== target-num:
                if len(data[num])>1:
                    pair = data[num][:2]
                    cmax = max(cmax, num)
            else:
                pair = [data[num][0], data[target-num][0]]
                cmax = max(num, cmax, target-num)

    return pair

assert find_pair_given_sum([1, 10, 25, 35, 60], 90) == [2,3]
assert find_pair_given_sum([20, 50, 40, 25, 30, 10], 90)==[1,5]