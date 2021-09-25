class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # we can use hashmap to solve this problem 
        # lc soltuion: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/discuss/686335/JavaPython-3-Greedy-Alg.%3A-3-methods-from-O(nlogn)-to-O(n)-w-brief-explanation-and-analysis.
        
        """
        Count the occurrences of each number using HashMap;
        Using Array to count each occurrence, since max occurrence <= arr.length;
        From small to big, for each unvisited least frequent element, deduct from k the multiplication with the number of         elements of same occurrence, check if reaching 0, then deduct the correponding unique count remaining.
        """
        
        c = Counter(arr) # use Counter to find frequncy of num in arr
        cnt, remaining = Counter(c.values()), len(c) # cnt contain each freqncy's num, eg 2 2len num, remaining countain all remaining nums
        for key in range(1, len(arr) + 1): # iterate the frequency of nums, maximum is len(arr) +1 (all same num)
            if k >= key * cnt[key]: # if we can elimiate a num
                k -= key * cnt[key] # elimiate them all
                remaining -= cnt[key]
            else:
                return remaining - k // key
            """
            say, remaining = 5 numbers, remaining k = 3, and currently occur = 3. occurenceCount[3] = 2.
            So, there are 2 numbers that have a frequency of 3, but there's only 3 left of k. So the remaining will be = 5             - (3/3) = 4. Because out of the two numbers that occur 3x, I can only remove 1."""
        return remaining
    # time O(n) Space O(n)