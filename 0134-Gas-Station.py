'''
If car starts at A and can not reach B. Any station between A and B
can not reach B.(B is the first station that A can not reach.)
If the total number of gas is bigger than the total number of cost. There must be a solution.
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_cost = 0
        sum_gas = 0
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i +1
                tank = 0
        
        if sum_gas - sum_cost < 0:
            return -1
        else:
            return start