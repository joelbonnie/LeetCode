import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for currentToken in tokens: 
            if currentToken not in "+-*/": 
                numStack.append(int(currentToken))
            else:
                secondOperand = numStack.pop()
                firstOperand = numStack.pop() 
                result = 0 
                match currentToken: 
                    case "+":
                        result = firstOperand + secondOperand
                    case "-":
                        result = firstOperand - secondOperand
                    case "*":
                        result = firstOperand * secondOperand
                    case "/":
                        result = math.trunc(firstOperand / secondOperand)
                
                numStack.append(result)
        return numStack.pop()
