"""
https://leetcode.com/discuss/interview-question/370112

Approach:
Use sliding window approach and ensure that length of set of each sliding window is same as length of sliding window. This would ensure that characters of the string are unique. Also for storing result use set to avoid duplicate and convert set to list and return the result.

Time Complexity: O(N*K)
Space Complexity: O(N)
"""

def unique_substring(string, k):
    res = set()

    for i in range(0, len(string)+1-k):
        if len(string[i:i+k]) == len(set(string[i:i+k])):
            res.add(string[i:i+k])

    return list(res)

assert set(unique_substring("abcabc", 3)) == set(["abc", "bca", "cab"])
assert set(unique_substring("abacab", 3)) == set(["bac", "cab"])
assert set(unique_substring("awaglknagawunagwkwagl", 4)) == set(["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"])
