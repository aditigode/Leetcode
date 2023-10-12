class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    
    def create_trie(self, products):
        #head = self.root
        for product in products:
            head = self.root
            #print(head.children)
            #print(product)
            for letter in product:
                if letter not in head.children.keys():
                    head.children[letter] = TrieNode()
                head = head.children[letter]
            head.isWord = True

    def find_word(self, word):
        head = self.root
        self.res = []
        for letter in word:
            if letter not in head.children:
                return self.res
            head = head.children[letter]
        if head.isWord:
            self.res.append(word)

        self.dfs(head, word)
        #print("res is",self.res)
        if len(self.res) > 3:
            return self.res[:3]
        return self.res

    def dfs(self,node, word):
        for child in node.children:
            #print(node.children.keys(), child)
            if node.children[child].isWord:
                self.res.append(word+child)
            if node.children[child]:
                self.dfs(node.children[child], word+child)
        


                
                
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        self.root = TrieNode()
        self.create_trie(products)
        search = ""
        result = []
        for letter in searchWord:
            #print("letter is", letter, search+
            search += letter
            #print(search)
            result.append(self.find_word(search))

        return result

        

        