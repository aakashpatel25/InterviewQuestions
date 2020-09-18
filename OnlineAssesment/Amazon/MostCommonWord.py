"""
https://leetcode.com/problems/most-common-word/

Approach:
Convert block words to set for easy lookup and convert paragraph to lower case to remove case sensitivity
Use regular expression to extract words from the paragraph and then use collections.Counter to count frequency and remove the block words from the frequency table.
Return most common word using most_common() function of the counter.

Time Compexity: O(N) - Looping over each word couple of times
Space Complexity: O(N) - Storing each word in the list

For detailed test suite: https://leetcode.com/problems/most-common-word/
"""
import collections

def get_most_common_word(paragraph, block):
    if paragraph == "": return None
    block = set(block)

    import re
    words = re.findall("[a-z]+", paragraph.lower())
    words = [ele for ele in words if ele not in block]
    return collections.Counter(words).most_common()[0][0]
    # data = {key:val for key, val in collections.Counter(words).items() if key not in block}
    # return collections.Counter(data).most_common()[0][0]

res1 = get_most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
assert res1 == "ball"