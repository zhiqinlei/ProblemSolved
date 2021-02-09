class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in nums:
            if l < 2 or i > nums[l-2]:
                nums[l] = i
                l += 1
                
        return l


'''
this solution can be easily generalized to "at most K duplicates"
int removeDuplicates(vector<int>& nums, int k) {
    int i = 0;
    for (int n : nums)
        if (i < k || n > nums[i-k])
            nums[i++] = n;
    return i;
}
'''