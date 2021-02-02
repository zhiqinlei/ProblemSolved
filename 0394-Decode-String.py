# 0394-Decode-string.py
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = 0
        current_string = ''
        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            elif c == '[':
                stack.append((current_string, k))
                current_string = ''
                k = 0
            elif c == ']':
                last_string, n = stack.pop(-1)
                current_string = last_string + n*current_string
            else:
                current_string += c
        
        return current_string