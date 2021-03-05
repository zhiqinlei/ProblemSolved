'''
Same simple algorithm written in every offered language. Variable a tells you the number of ways to reach the current step, and b tells you the number of ways to reach the next step. So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b, since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.

Based on Fibonacci, formula a+b, where a+b becomes the b of the next computation(b += a) ,and b becomes the a of the next computation(a = b+a-a).
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a+b
        return a