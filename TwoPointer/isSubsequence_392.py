class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s: return True 
        if not t: return False 
        
        s_pointer = 0 
        t_pointer = 0 

        while s_pointer <= len(s) - 1 and t_pointer <= len(t) - 1: 
            if s[s_pointer] == t[t_pointer]: 
                s_pointer += 1
            t_pointer += 1 
        
        if s_pointer != len(s): 
            return False
        return True 


        
        # Follow up: 
        # Create char - index list map 
        # O(t) * k for current approach vs 
        # O(t) + k * O(s * logt) for map + binary search for each char in s 
