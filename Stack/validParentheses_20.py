class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketMap = {'{':'}', '[':']', '(':')'}
        bracketStack = []

        for currentChar in s:

            if currentChar in '{[(':
                bracketStack.append(currentChar)

            else:
                if not bracketStack:
                    return False
                elif bracketMap[bracketStack.pop()] != currentChar:
                    return False
        
        if bracketStack:
            return False
        return True



sol = Solution()
print(sol.isValid("(())"))
print(sol.isValid("[)"))
print(sol.isValid("[{}]()"))
