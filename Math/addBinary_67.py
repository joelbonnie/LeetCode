class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        carry = 0 
        resultSum = ""

        for i in range(max(len(a), len(b))):
            firstDigit = int(a[i]) if i < len(a) else 0
            secondDigit = int(b[i]) if i < len(b) else 0

            newDigit = firstDigit + secondDigit + carry 
            resultSum = str(newDigit % 2) + resultSum 
            carry = newDigit // 2

        if carry:
            resultSum = "1" + resultSum
            
        return resultSum 

