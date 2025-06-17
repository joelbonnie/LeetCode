class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        chrCounts = [0] * 26 
        maxF = 0

        maxLen = 0 

        for r in range(0, len(s)):
            chrCounts[ord(s[r]) - 65] += 1
            maxF = max(maxF, chrCounts[ord(s[r]) - 65])

            while ((r - l + 1) - maxF) > k: 
                chrCounts[ord(s[l]) - 65] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
