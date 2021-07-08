class Solution:

    def __init__(self, nums: List[int]):
        self.record = {}
        for idx, x in enumerate(nums):
            if x not in self.record:
                self.record[x] = [idx]
            else:
                self.record[x].append(idx)

    def pick(self, target: int) -> int:
        return self.record[target][randint(0,len(self.record[target])-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
