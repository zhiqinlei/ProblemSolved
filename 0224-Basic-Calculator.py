class Solution:
    def calculate(self, s: str) -> int:
        ans, num, sign, stack = 0, 0, 1, [1]
        
        for i in s+"+": # add the last element
            if i.isdigit():
                num = 10*num + int(i)
            elif i in "-+":
                ans += num * sign * stack[-1]
                sign = 1 if i == "+" else -1
                num = 0
            elif i == "(":
                stack.append(sign*stack[-1])
                sign = 1
            elif i == ")":
                ans += num * sign * stack[-1]
                num = 0
                stack.pop()
        return ans
