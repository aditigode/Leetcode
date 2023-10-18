class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergeStr= ""
        #print(word1[1:])
        i, j = 0, 0
        count = 0
        while i < len(word1) and j < len(word2):
            if count % 2 == 0:
                mergeStr += word1[i]
                i += 1
            else:
                mergeStr += word2[j]
                j += 1
            count += 1

        if i < len(word1):
            mergeStr += word1[i:]
        elif j < len(word2):
            mergeStr += word2[j:]

        return mergeStr



        