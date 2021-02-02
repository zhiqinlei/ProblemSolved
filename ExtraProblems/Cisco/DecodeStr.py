s = input()
stack = []
stack2= []
k = 0
current_str = ''

for c in s:
    if c.isdigit():
        k = k*10 + int(c)
        stack2.append(k)
    
    elif c == '(':
        stack.append(current_str)
        current_str = ''
    
    elif c.isalpha():
        current_str += c
    
    elif c == '{':
        k = 0

    elif c == '}':
        last_str = stack.pop(-1)
        n = stack2.pop(-1)
        current_str = last_str + n*current_str

print(current_str)