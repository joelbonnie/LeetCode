from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineHashMap = Counter(magazine)
        for currentLetter in ransomNote: 
            if magazineHashMap.get(currentLetter):
                magazineHashMap[currentLetter] -= 1
                if magazineHashMap[currentLetter] < 0:
                    return False
            else:
                return False
        return True 
