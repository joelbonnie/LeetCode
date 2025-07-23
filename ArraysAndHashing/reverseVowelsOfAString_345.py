class Solution:
    def reverseVowels(self, s: str) -> str:
        # Two passes 

        vowelList = []
        stringList = list(s)

        for i in range(len(s)): 
            if stringList[i].lower() in "aeiou":
                vowelList.append(stringList[i])
                stringList[i] = None
        
        for i in range(len(s)):
            if stringList[i] is None: 
                stringList[i] = vowelList.pop()
        
        return ''.join(stringList)
