import sys
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.children = defaultdict(TrieNode)



class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total_cnt = 0

    def insert_tree(self, tree: str) -> None:
        node = self.root
        for char in tree:
            node = node.children[char]
        node.cnt += 1
        self.total_cnt += 1

    def show_result(self) -> None:
        node = self.root
        self.dfs(node, '')
    
    def dfs(self, node: TrieNode(), prefix: str) -> None:
        if node.cnt > 0:
            print("%s %.4f" % (prefix, (node.cnt / self.total_cnt * 100)))
        
        for char in sorted(node.children.keys()):
            self.dfs(node.children[char], prefix + char)

trie = Trie()
trees = sys.stdin.readlines()
for tree in trees:
    trie.insert_tree(tree.strip())

trie.show_result()