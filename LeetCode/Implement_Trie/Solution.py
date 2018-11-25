class TrieNode:
        def __init__(self):
            self.word = False
            self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    def startsWith(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("abstract")
    trie.insert("boolean")
    trie.insert("lover")
    print(trie.search("abstract"))
    print(trie.search("app"))
    print(trie.startsWith("bro"))
