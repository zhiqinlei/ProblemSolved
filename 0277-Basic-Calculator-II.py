class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, '+'
    
        for i in range(len(s)):
        
            if s[i].isdigit():
                num = (num * 10) + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
            
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    p = stack.pop()
                    res = abs(p) // num
                    stack.append(res if p >= 0 else -res)
                num = 0
                sign = s[i]
            
        return sum(stack)
***
def calculate(self, s):
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)           #for BC II and BC III
            if op == "/": stack.append(int(stack.pop() / v))      #for BC II and BC III

        it, num, stack, sign = 0, 0, [], "+"

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":                                        # For BC I and BC III
                num, j = self.calculate(s[it + 1:])
                it = it + j
            elif s[it] == ")":                                        # For BC I and BC III
                update(sign, num)
                return sum(stack), it + 1
            it += 1
        update(sign, num)
        return sum(stack)
***
