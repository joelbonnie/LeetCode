class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenSet = set()
        l = 0 
        maxLen = 0

        for r in range(len(s)):
            while s[r] in seenSet:
                seenSet.remove(s[l])
                l += 1
            seenSet.add(s[r])
            maxLen = max(maxLen, r-l + 1)
            
        return maxLen
