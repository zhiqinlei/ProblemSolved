class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        # quick sort
        pivot = random.choice(nums)
        left, mid, right = [],[],[]
        for i in nums:
            if i >pivot:
                left.append(i)
            elif i < pivot:
                right.append(i)
            else:
                mid.append(i)
        l = len(left)
        m = len(mid)
        
        if k <= l:
            return self.findKthLargest(left, k)
        elif k > l+m:
            return self.findKthLargest(right, k-l-m)
        else:
            return mid[0]
#https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained       
