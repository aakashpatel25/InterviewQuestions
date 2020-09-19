"""
https://leetcode.com/problems/partition-labels/

Approach:
Just figure out starting and ending position of each character. Merge character's intervals having overlapping positons.

Compute length of each intervals and return the list of it.

Time Complexity: O(N) (Note: sorting and merging would take constant time here as there can be only 26 intervals)
Space Complexity: O(1) (Note: data dictionary and intervals list will have at max 26 elements each hence O(52) = O(1))
"""

def partitionLabels(S):
    data = {}
    for i,ele in enumerate(S):
        if ele in data:
            data[ele][1] = i+1
        else:
            data[ele] = [i,i+1]

    interval = sorted(data.values())
    counter = 0

    while counter < len(interval)-1:
        if interval[counter][1] > interval[counter+1][0]:
            interval[counter][0] = min(interval[counter][0], interval[counter+1][0])
            interval[counter][1] = max(interval[counter][1], interval[counter+1][1])
            del interval[counter+1]
        else:
            counter+=1

    return [ele[1]-ele[0] for ele in interval]


assert partitionLabels("ababcbacadefegdehijhklij") == [9,7,8]