class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        while len(ans) <= n:
            ans += [i+1 for i in ans]
        return ans[:n+1]

//Code works by constantly extending a list with itself but with the values incremented by 1. and pick lst from index 0 to n
