num = int(input())
if num == 0:
    print(0)

result = 0
while(num):
    num &= num-1
    result += 1

print(result)