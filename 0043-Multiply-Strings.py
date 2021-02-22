class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0]*(len(num1)+len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                ans[i+j] += int(e1)*int(e2)
                ans[i+j+1] += ans[i+j]//10
                ans[i+j] %= 10
            
        while len(ans)>1 and ans[-1] == 0: ans.pop()
        return ''.join(map(str, ans[::-1]))

# with comments
class Solution:
    def multiply(self, num1, num2):
        product = [0] * (len(num1) + len(num2)) #placeholder for multiplication ndigit by mdigit result in n+m digits
        position = len(product)-1 # position within the placeholder

        for n1 in num1[::-1]:
            tempPos = position 
            for n2 in num2[::-1]: 
                product[tempPos] += int(n1) * int(n2) # ading the results of single multiplication
                product[tempPos-1] += product[tempPos]//10 # bring out carry number to the left array
                product[tempPos] %= 10 # remove the carry out from the current array
                tempPos -= 1 # first shifting the multplication to the end of the first integer
            position -= 1 # then once first integer is exhausted shifting the second integer and starting 


        # once the second integer is exhausted we want to make sure we are not zero padding  
        pointer = 0 # pointer moves through the digit array and locate where the zero padding finishes
        while pointer < len(product)-1 and product[pointer] == 0: # if we have zero before the numbers shift the pointer to the right
            pointer += 1

        return ''.join(map(str, product[pointer:])) # only report the digits to the right side of the pointer

# no int func
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i, v1 in enumerate(reversed(num1)):
            for j, v2 in enumerate(reversed(num2)):
                int1 = ord(v1) - ord('0')
                int2 = ord(v2) - ord('0')
                res[i + j] += int1 * int2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join(str(v) for v in res)[::-1]