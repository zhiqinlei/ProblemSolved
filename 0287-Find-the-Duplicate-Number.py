class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # many methods of solutions
        # use slow,fast pointer to solve
        # https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions%3A-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained
        # https://leetcode.com/problems/find-the-duplicate-number/discuss/73022/Python-Solution-with-O(1)-space-and-O(nlogn)-time
        slow  = 0
        fast = nums[0] # fast at the next stage of slow
        
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]] # slow one step, fast two step until they meet
        
        fast = nums[slow]
        slow = 0 # once they meet, move fast to slow's next stage, move slow to start position
        
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast] # move both one step until they meet again
        
        return slow # we found the start position of loop
    # O(n) Time O(1) Space
