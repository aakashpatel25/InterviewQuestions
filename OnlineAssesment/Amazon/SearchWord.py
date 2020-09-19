"""
https://leetcode.com/problems/search-suggestions-system/

Approach:
Use Tries to create tree like word structure. Use DFS to then look for words that matches the existing prefix and return set of results. Involvs lot of recomputation.

Can use for loops onver sorted list of products and then each time filter out the products that have been already been filtered.

Time Complexity: O(N*N)
Space Complexity: O(N)
"""
class TrieNode:
    def __init__(self):
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        tmp = self.root
        for char in word:
            if char not in tmp.child:
                tmp.child[char] = TrieNode()
            tmp = tmp.child[char]
        tmp.child["*"] = TrieNode()

    def search(self, word):
        res = []
        tmp  = self.root
        for char in word:
            if char not in tmp.child:
                return res
            tmp = tmp.child[char]

        def dfs(node, prefix):
            for char, node in sorted(node.child.items()):
                if char == "*":
                    res.append(prefix)
                else:
                    dfs(node, prefix+char)
        dfs(tmp, word)
        return res[:3]


def suggestedProductsTries(products, searchWord):
    trie = Trie()
    for prod in products:
        trie.insert(prod)

    res = []
    for i in range(1, len(searchWord)+1):
        res.append(trie.search(searchWord[:i]))

    return res


def suggestedProducts(products, searchWord):
    prod = sorted(products)
    prev = prod
    res  = []

    for i, char in enumerate(searchWord):
        searchRes = [ele for ele in prev if len(ele) > i  and ele[i]==char]
        prev = searchRes
        res.append(searchRes[:3])

    return res


products = ["mobile","mouse","moneypot","monitor","mousepad"]
assert suggestedProductsTries(products, "mouse") == [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]

assert suggestedProducts(products, "mouse") == [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]


assert suggestedProductsTries(["havana"], "havana") == [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

assert suggestedProducts(["havana"], "havana") == [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

assert suggestedProductsTries(["bags","baggage","banner","box","cloths"], "bags") == [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

assert suggestedProducts(["bags","baggage","banner","box","cloths"], "bags") == [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

assert suggestedProductsTries(["havana"], "tatiana") == [[],[],[],[],[],[],[]]
assert suggestedProducts(["havana"], "tatiana") == [[],[],[],[],[],[],[]]