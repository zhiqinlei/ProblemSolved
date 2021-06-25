class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        l1, l2 = 0, 0
        while l1 < n1 and l2 < n2:
            if nums1[l1] < nums2[l2]:
                l1 += 1
            elif nums1[l1] > nums2[l2]:
                l2 += 1
            else:
                ans.append(nums1[l1])
                l1 += 1
                l2 += 1
        return ans
