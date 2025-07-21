class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""

        i = 0 
        while i < min(len(word1), len(word2)):
            mergedString += (word1[i] + word2[i])
            i += 1

        if i < len(word1): 
            mergedString += word1[i:]
        elif i < len(word2):
            mergedString += word2[i:]
        
        return mergedString

