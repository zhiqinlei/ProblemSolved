class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m >0 and n>0: # check one by one
            if nums1[m-1] > nums2[n-1]: # if num1 > num2, switch to back
                nums1[m-1+n] = nums1[m-1]
                m -=1
            else:
                nums1[m-1+n] = nums2[n-1]
                n -=1
        
        if n >0: # nums2 still have num not add to nums1, replace their end n elements
            nums1[:n] = nums2[:n]
#https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
