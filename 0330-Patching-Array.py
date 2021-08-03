class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # use greedy algorithm to solve
        # find the smallest x patch every time, if x, next patch must be > 2x
        # china lc solution
        ans = 0
        x, length, idx = 1, len(nums), 0 # x start as the smallest int 1
        
        while x <= n:
            if idx < length and nums[idx] <= x: # if x is include
                x += nums[idx]                  # increase x by nums[idx]
                idx += 1
            else:                               # if not, add x patch
                x *= 2 # same as x <<= 2
                ans += 1
        return ans
    # O(m+logn) Time, m is the length of nums, loop log n because n > x*2
    # O(1) Space
