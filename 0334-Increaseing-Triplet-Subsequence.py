class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Trick Solution
        # https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
        # Start with the maximum numbers for the first and second element. Then:
        #(1) Find the first smallest number in the 3 subsequence
        #(2) Find the second one greater than the first element, reset the first one if it's smaller
        
        # we can use two thresholds to divide the subsquence length
        # everything between threshold1 and threshold2 will form doublets
        # everything above threshold2 will form a triplet
        # dynamically change these two thresholds
        small = mid = float("inf")
        for i in nums:
            if i <= small: # must be <=
                small = i
            elif i <= mid:
                mid = i
            else:
                return True
        return False
    # O(n) Time, O(1) Space
