class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1Map = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        s2Map = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for r in range(len(s1)):
            s1Map[s1[r]] += 1
            s2Map[s2[r]] += 1
        
        if s1Map == s2Map:
            return True
        
        l = 0 
        r = len(s1)

        while r < len(s2):
            s2Map[s2[l]] -= 1
            s2Map[s2[r]] += 1
            if s1Map == s2Map:
                return True
            l += 1
            r += 1 


        return False
