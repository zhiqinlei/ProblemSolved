class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # hard problem, use binary search and recursive to solve
        # three solutions
        # https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
        
        # find the median sorted array
        length = len(nums1) + len(nums2)
        if length % 2 == 1: # odd
            return self.kthSmallest(nums1, nums2, length//2)
        else: # even
            return (self.kthSmallest(nums1, nums2, length//2) + self.kthSmallest(nums1, nums2, length//2 -1)) /2
        
    def kthSmallest(self, a, b, k): # find the kth smallest num in merged [ab]
            if not a:
                return b[k]
            if not b:
                return a[k] # base case
            
            idxA, idxB = len(a)//2, len(b)//2
            medianA, medianB = a[idxA], b[idxB] # find the median value and idx of a,b
            
            # if k > sum of a,b median indices
            if k > idxA + idxB:
                # if median A > median B, B's first half does not include K
                if medianA > medianB:
                    return self.kthSmallest(a, b[idxB +1:], k - idxB -1)
                else:
                    return self.kthSmallest(a[idxA +1:], b, k - idxA -1)
            # if k < sum of a,b median indices
            else:
                # if medianA > medianB, A's second half does not include k
                if medianA > medianB:
                    return self.kthSmallest(a[:idxA], b, k)
                else:
                    return self.kthSmallest(a, b[:idxB],k)
        # O(log (m+n)) Time, O(1) Space
