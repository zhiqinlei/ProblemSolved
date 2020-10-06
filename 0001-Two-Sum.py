# 0001-Two-Sum.py

# Solution 1 time O(n) Space O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1, l):
                if nums[i]+nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans

# Solution 2 better solution
def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n          # m is the complement of n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i