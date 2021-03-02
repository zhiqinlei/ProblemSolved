class Solution(object):
    def combinationSum3(self, k, n):
        ret = []
        self.dfs(list(range(1, 10)), k, n, [], ret)
        return ret
    
    def dfs(self, nums, k, n, path, ret):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ret)

'''
He is amazing that he passed the list from 1 to 9 as a variable so next time when he calls the list of number candidates they start off from numbers that haven't been seen,
For example: normally for 3, 7 you will get [[1,2,4], [1,4,2], [2,1,4] etc...
Using his way of doing it avoid adding the identical list into the final result this and it is just brilliant.

I have added the slow code in reply if you don't see what I am talking about
'''