class TrieNode:
    def __init__(self):
        self.wordDict = {}
        self.isWord = False
        
class Trie:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            #print(char,curr)
            if char not in curr.wordDict:
                curr.wordDict[char] = TrieNode()
            curr = curr.wordDict[char]
        curr.isWord = True
        return
    

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char in curr.wordDict:
                curr = curr.wordDict[char]
            else:
                return False
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char in curr.wordDict:
                curr = curr.wordDict[char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)