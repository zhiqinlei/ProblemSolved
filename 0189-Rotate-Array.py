'''
answer link: https://leetcode.com/problems/rotate-array/discuss/54426/Summary-of-solutions-in-Python

Classical 3-step array rotation:

reverse the entire array

reverse the first n - k elements

reverse the rest of them


'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums)-1
        k = k % len(nums)
        
        nums.reverse()
        self.reverse(0, k-1, nums)
        self.reverse(k, end, nums)
        
    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# O(n) in time, O(1) in space
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        for i in xrange(0, k):
            tmp = nums[-1]
            for j in xrange(0, len(nums) - 1):
                nums[len(nums) - 1 - j] = nums[len(nums) - 2 - j]
            nums[0] = tmp