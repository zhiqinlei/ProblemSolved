S = '1??13'

ch = ['1', '2', '3']
L = list(S)

print(L)

for i in range(len(L)):
    if L[i] == '?':
        if i == 0:
            for j in ch:
                if j != L[i+1]:
                    L[i] = j
                    break
        elif i == len(L)-1:
            for j in ch:
                if j != L[i-1]:
                    L[i] = j
                    break
        else:
            for j in ch:
                if j != L[i-1] and j != L[i+1]:
                    L[i] = j
                    break

result = ''
for i in L:
    result += i

print(result)