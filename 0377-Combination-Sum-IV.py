    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                combs[i] += combs[i - num]
        return combs[target]

#explain
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]

# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 116 ms
This is a 4-line top-down solution that doesn't get accepted due to recursion limit.

class Solution(object):
    def combinationSum4(self, nums, target, memo=collections.defaultdict(int)):
        if target < 0: return 0
        if target not in memo:
            memo[target] += sum((1, self.combinationSum4(nums, target - num))[target != num] 
                                for num in nums)
        return memo[target]
The problem with negative numbers is that now the combinations could be potentially of infinite length. Think about nums = [-1, 1] and target = 1. We can have all sequences of arbitrary length that follow the patterns -1, 1, -1, 1, ..., -1, 1, 1 and 1, -1, 1, -1, ..., 1, -1, 1 (there are also others, of course, just to give an example). So we should limit the length of the combination sequence, so as to give a bound to the problem.

This is a recursive Python code that solves the above follow-up problem, so far it's passed all my test cases but comments are welcome.

class Solution(object):
    def combinationSum4WithLength(self, nums, target, length, memo=collections.defaultdict(int)):
        if length <= 0: return 0
        if length == 1: return 1 * (target in nums)
        if (target, length) not in memo: 
            for num in nums:
                memo[target, length] += self.combinationSum4(nums, target - num, length - 1)
        return memo[target, length]
'''
#dp solution
'''
Explanation: Take the example in the question, where nums is [1, 2, 3] and the target is 4. Here's how you would build the solution bottom up by starting with the ways you can make a total of 1, then the number of ways you can make a total of 2, and so on up to 4:

1 -> [1]
2 -> [1, 1], [2]
3 -> [1, 1, 1], [1, 2], [2, 1], [3]
4 -> [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]

Since we just need the counts, not the actual combinations, this can be simplified to the following DP algorithm:

Pre-Step: Initialize the DP array to be 1 for each number in nums (since you can trivially make that total by just using that number itself) and 0 otherwise.
DP = [0, 1, 1, 1, 0]

Now for each number on the way to our target, call that sub-target t_sub. See how many ways we can make t_sub by taking each number n in nums and checking how many ways we were able to make t_sub - n then adding that to the DP entry for t_sub.

Step 1:
t_sub = 1
t_sub - 1 = 0 so add nothing
t_sub - 2 < 0 so add nothing
t_sub - 3 < 0 so add nothing
DP = [0, 1, 1, 1, 0]

Step 2:
t_sub = 2
t_sub - 1 = 1 so DP[2] += DP[1] and is now 2
t_sub - 2 = 0 so add nothing
t_sub - 3 < 0 so add nothing
DP = [0, 1, 2, 1, 0]

Step 3:
t_sub = 3
t_sub - 1 = 2 so DP[3] += DP[2] and is now 3
t_sub - 2 = 1 so DP[3] += DP[1] and is now 4
t_sub - 3 = 0 so add nothing
DP = [0, 1, 2, 4, 0]

Step 4:
t_sub = 4
t_sub - 1 = 3 so DP[4] += DP[3] and is now 4
t_sub - 2 = 2 so DP[4] += DP[2] and is now 6
t_sub - 3 = 1 so DP[4] += DP[1] and is now 7
DP = [0, 1, 2, 4, 7]

Now we are finished, so return DP[-1], which is the number of ways we can make t_sub when t_sub is the target.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (1+target)
        for num in nums:
            if num <= target:
                dp[num] = 1
        for i in range(target+1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i-num]
        return dp[-1]
'''