class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations, reverse = True) # sorted not sort
        h = 0
        i = 0
        n = len(citations)
        while i < n and h < sorted_citations[i]: # h < sorted citations[i], at least has h +1 
            i += 1
            h += 1
        return h
    
    # time complexity nlogn, the complexity of sort algorithm
    # space log n 
