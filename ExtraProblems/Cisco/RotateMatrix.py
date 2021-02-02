n = int(input())
M = []

for i in range(n):
    line = input()
    row = line.splite(' ')
    M.append(row)

M.reverse()
for i in range(len(M)):
    for j in range():
        M[i][j], M[j][i] = M [j][i], M[i][j]

for i in M:
    print(' '.join(i))