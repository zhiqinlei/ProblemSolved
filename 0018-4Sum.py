class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #https://leetcode.com/problems/4sum/discuss/1341213/C%2B%2BPython-2-solutions-Clean-and-Concise-Follow-up%3A-K-Sum
        # sort and two pointer
        '''
        Sort nums in increasing order.
We fix nums[i], nums[j] by iterating the combination of nums[i], nums[j], then the problem now become to very classic problem 1. Two Sum.
By using two pointers, one points to left, the other points to right, remain = target - nums[i] - nums[j].
If nums[left] + nums[right] == remain
Found a valid quadruplets
Else if nums[left] + nums[right] > remain
Sum is bigger than remain, need to decrease sum by right -= 1
Else:
Increasing sum by left += 1.

        '''
        '''
        ans = set()
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            for j in range(i+1, n):
                left, right = j+1, n-1
                remain = target - nums[i] - nums[j]
                while left < right:
                    if remain > nums[left] + nums[right]:
                        left += 1
                    elif remain < nums[left] + nums[right]:
                        right -=1
                    else:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left +=1
                        right -=1
        return ans
    
    # O(n3) time, O(sort) space
    '''
        def dfs(l, r, k, target, path, out):  # [l, r] inclusive
            if k == 2:
                while l < r:
                    if nums[l] + nums[r] == target:
                        out.append(path + [nums[l], nums[r]])
                        while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[l]
                        l, r = l + 1, r - 1
                    elif nums[l] + nums[r] > target:
                        r -= 1  # Decrease sum
                    else:
                        l += 1  # Increase sum
                return

            while l < r:
                dfs(l+1, r, k - 1, target - nums[l], path + [nums[l]], out)
                while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[i]
                l += 1

        def kSum(k):  # k >= 2
            ans = []
            nums.sort()
            dfs(0, len(nums)-1, k, target, [], ans)
            return ans

        return kSum(4)
    # time O(NlogN + N^(k-1)), where k >= 2, N is number of elements in the array nums
    # space O(N)