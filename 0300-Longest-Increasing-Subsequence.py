class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lc cn solution, we can use dp to solve this problem
        # https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
        # or patient sorting soltuion: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
        
        # we use a dp to record longest increasing subsequence in nums[i], then we iterate 0-i to check the longest subsequence less than i
        """
        if not nums:
            return 0
        
        dp = []
        
        for i in range(len(nums)):
            dp.append(1) # base case, start with length 1
            for j in range(i): # iterate from idx 0 to i
                if nums[j] < nums[i]: # if nums[j] is less than nums[i], the longest increasing subsequence of i will update
                    dp[i] = max(dp[i], dp[j]+1) # we will pick the longest increasing subsequence
        return max(dp) # find the longest increasing subsequence in the nums
        """
    
    # Time O(n2) two iterations, Spcae O(n)
    
    # Greedy + binary search
    
        # use d[i] to record the smallest element in len i subsequence
        d = [] # d to record longest increasing subsequnce
        for n in nums:
            if not d or n > d[-1]: # if n> last element, add it
                d.append(n)
            else:                  # if not, n might less than some element in d, use binary search to find it
                l, r = 0, len(d) - 1 
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n: # if find n less than d[j], continue update until we find the smallest location
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
    # Time O(nlogn), space O(n)

