def isValid(s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            if i == ")":
                if stack == []:
                    return False
                temp = stack.pop()
                if temp != "(":
                    return False
            if i == "]":
                if stack == []:
                    return False
                temp = stack.pop()
                if temp != "[":
                    return False
            if i == "}":
                if stack == []:
                    return False
                temp = stack.pop()
                if temp != "{":
                    return False
            
        if stack != []:
            return False
        return True

print(isValid("]"))