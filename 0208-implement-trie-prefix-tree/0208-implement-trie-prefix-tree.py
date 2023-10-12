class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        head = self.root
        for letter in word:
            if letter not in head.children:
                head.children[letter] = TrieNode()
            head = head.children[letter]
        head.isWord = True

        

    def search(self, word: str) -> bool:
        head = self.root
        for letter in word:
            if letter not in head.children:
                return False
            head = head.children[letter]
        return head.isWord

        

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for letter in prefix:
            if letter not in head.children:
                return False
            head = head.children[letter]

        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)