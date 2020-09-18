"""
https://leetcode.com/discuss/interview-question/542597/

Approach:
Convert keyword list into set for O(1) lookup. Convert all reviews into lowercase to remove case-sensetivity of words. Use regular expression to extract each words in the reivew and use set to remove duplicate words in each review. For each reivew add list of unique words that are keywords to default dictionary word frequency.

Sort the default dictionary by values and return most popular K words

Time Complexity: O(N*M + NlogN)
Space Complexity: O(N)
"""
import re

def get_k_popular_keywords(k, keywords, reviews):
    word_freq = collections.defaultdict(int)
    keywords = set(keywords)

    for review in reviews:
        words = list(set(re.findall("[a-z]+", review.lower())))
        for word in words:
            if word in keywords:
                word_freq[word]+=1

    word_freq = sorted(word_freq.items(), key=lambda item:(-item[1], item[0]))
    return [word for word, _ in word_freq[:k]]

actual1 = get_k_popular_keywords(2, ["anacell", "cetracular", "betacellular"],
                [
                    "Anacell provides the best services in the city",
                    "betacellular has awesome services",
                    "Best services provided by anacell, everyone should use anacell",
                ]
            )

actual2 = get_k_popular_keywords(2, ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],
                [
                    "I love anacell Best services; Best services provided by anacell",
                    "betacellular has great services",
                    "deltacellular provides much better services than betacellular",
                    "cetracular is worse than anacell",
                    "Betacellular is better than deltacellular.",
                ]
            )

assert actual1 == ["anacell", "betacellular"]
assert actual2 == ["betacellular", "anacell"]