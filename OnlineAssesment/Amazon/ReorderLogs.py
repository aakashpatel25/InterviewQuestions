"""
https://leetcode.com/problems/reorder-data-in-log-files/

Approach:
Split logs using split function. Identify letter and string logs. Sort letter logs and combine letter and digit logs.

Time Complexity: O(klogk + n)
Space Complexity: O(2N)
"""

def reorderLogFiles(logs):
    logs = [ele.split(" ", 1) for ele in logs]
    letter = [ele for ele in logs if ele[1].split()[0].isalpha()]
    digit = [ele for ele in logs if ele[1].split()[0].isdigit()]

    letter.sort(key=lambda item:(item[1], item[0]))
    letter = [" ".join(ele) for ele in letter]
    return letter + [" ".join(ele) for ele in digit]

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
expect = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
assert reorderLogFiles(logs) == expect