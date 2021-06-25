class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) <len(set2):
            for i in set1:
                if i in set2:
                    ans.append(i)
        else:
            for i in set2:
                if i in set1:
                    ans.append(i)
        return ans
