class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
                
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == "+":
                    stack.append(num1+num2)
                if i == "-":
                    stack.append(num1-num2)
                if i == "*":
                    stack.append(num1*num2)
                if i == "/":
                    stack.append(int(num1/num2)) # not // will truncate to zero
        
        return stack.pop()
