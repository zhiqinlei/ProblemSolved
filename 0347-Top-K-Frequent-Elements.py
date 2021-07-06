class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dic = {}
        frq = {}
        for n in nums:
            if dic.get(n) == None:
                dic[n] = 1
            else:
                dic[n] += 1
                              
        for key, value in dic.items():
            if value not in frq:
                frq[value] = [key]
            else:
                frq[value].append(key)
        
        for x in range(len(nums), 0, -1):
            if x in frq:
                for j in frq[x]:
                    ans.append(j)
        
        return ans[:k]

# https://leetcode.com/problems/top-k-frequent-elements/discuss/81697/Python-O(n)-solution-without-sort-without-heap-without-quickselect
