class Solution:
    def reverseWords(self, s: str) -> str:

        # Extra space 

        wordList = s.split()
        wordList.reverse()
        return ' '.join(wordList)
