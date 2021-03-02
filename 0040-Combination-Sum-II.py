class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(target, path, index):
            if target < 0:
                return
            if target == 0:
                res.append(path)
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]: # solve duplicate
                    continue
                dfs(target - candidates[i], path + [candidates[i]], i+1)
        dfs(target, [], 0)
        return res

'''
for example if you have candidates [1, 1, 1, 2] and target is 3, the output should be [[1, 1, 1,], [1,2]].
backtracking starts at index = 0 (i.e. Start with [1] and we want to find all combinations which adds up to 3, [1, 1, 1] and [1, 2]).
Once we are done with the first i = 0, we move on to i = 1
However since when i = 1, we also start with [1] (but with one less 1 compared to i = 0). We don't want to consider starting with another [1] because it will probably end up with duplication (in this case, we will get another [1,2])
Hence the condition is saying - "Hmmmm, I have seen 1 before. It's literally the last i I considered (since candidates is sorted), so I better keep incrementing i until i is no longer i".
'''