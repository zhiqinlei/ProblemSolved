def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)


'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)
Explanation
I will try to explain this solution by walking through the initial solution that I wrote:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
		for n in nums:
			result ^= n
		return result
The most crucial trick here is to recognize that if you XOR any same number together, you cancel it out (=0).
For example:
nums = [2,4,5,4,3,5,2]
XORing everything together
= 2 ^ 4 ^ 5 ^ 4 ^ 3 ^ 5 ^ 2
= (2^2) ^ (4^4) ^ (5^5) ^ 3
= 0 ^ 0 ^0 ^ 3
= 3

(If you are unfamiliar with the XOR operation, you can check out this stackoverflow post)

Now, let's go back to the one liner:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)
The reduce here just simplifies the previous for loop into one line, it's not doing anything different.
The initializer 0 is put there to prevent the the scenerio where nums is an empty list (I didn't realize that the question statement explicitly mentioned that it would be non-empty).
'''
