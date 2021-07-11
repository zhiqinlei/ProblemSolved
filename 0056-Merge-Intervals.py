class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the list[0] value first, then check if overlap happend, if yes, update. else, append it
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key = lambda x: x[0]) # use lambda to sort x[0] element
        res = [intervals[0]] # add the first element
        for n in intervals[1:]:
            if n[0] <= res[-1][1]:
                res[-1][1] = max(n[1], res[-1][1])
            else:
                res.append(n)
        return res
        
