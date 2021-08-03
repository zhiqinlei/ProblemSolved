class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # china lc solution
        # find all overlapping interval, merge into one big interval
        left, right = newInterval
        placed = False # check if newInterval placed
        ans = []
        
        for li, ri in intervals:
            if ri < left: # not overlap, in the left side, just place
                ans.append([li, ri])
            elif li > right: # not overalp, in the right side, check if newInterval placed
                if not placed: # if new interval not be placed, place it first
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            else: # if overlap, merge into one big interval, do not place
                left = min(left, li)
                right = max(right, ri)
        if not placed: # if newInterval in the end
            ans.append([left, right])
        return ans
    # O(n) Time, O(1) Space
