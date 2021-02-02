N = 5
A = [2,4]

result = ''

for i in range(N):
    if i in A:
        result += '+'
    else:
        result += '-'

#for j in A:
    #if result[j] == '-':
        #result[j] = '+'

print("result", result)