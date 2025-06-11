class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1]

        carry = 1

        for i in range(0, len(digits)):
            if carry:
                newDigit = digits[i] + carry 
                carry = newDigit // 10 
                digits[i] = newDigit % 10 
        
        if carry: 
            digits.append(1)
        
        return digits[::-1]
