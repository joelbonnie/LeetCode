class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            leftAlnumCheck = s[l].isalnum()
            rightAlnumCheck = s[r].isalnum()

            if not leftAlnumCheck:
                l += 1
            if not rightAlnumCheck:
                r -= 1
            
            if leftAlnumCheck and rightAlnumCheck:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

        
        return True
