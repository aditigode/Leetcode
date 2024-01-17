class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Dict = collections.Counter(word1)
        word2Dict = collections.Counter(word2)
        
        close = True
        #  c a bbb a: 
        # ccc aa b
        # a bb ccc
        
        # word1 and word2 should have all the same characters
        # count can be different
        # c: 1 a: 2 b:3
        # c : 3, a: 1 b:2
        return (sorted(word1Dict.keys()) == sorted(word2Dict.keys())) and (sorted(word1Dict.values()) == sorted(word2Dict.values()))
        
#         word1Letters,word1Count = [],[]
#         word2Letters, word2Count = [],[]
#         for letter,count in word1Dict.items():
#             word1Letters.append(letter)
#             word1Count.append(count)
        
#         for letter,count in word2Dict.items():
#             word2Letters.append(letter)
#             word2Count.append(count)
            
#         word1Letters.sort()
#         word2Letters.sort()
#         word1Count.sort()
#         word2Count.sort()
        
       # return word1Letters == word2Letters and word1Count == word2Count
        