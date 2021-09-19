class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # use map and backtracing to solve
        # https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode-solutio/
        # cn lc solution
        
        if not digits:
            return []
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backTracing(idx):
            if idx == len(digits): # find all comibnation
                res.append(''.join(combination))
            else:
                digit = digits[idx] 
                for letter in phoneMap[digit]: 
                    combination.append(letter)
                    backTracing(idx+1)
                    combination.pop() # avoid output ["ad","ade","adef","adefbd","adefbde","adefbdef","adefbdefcd","adefbdefcde","adefbdefcdef"]
            
        combination = []
        res = []
        backTracing(0)
        
        return res
    # time O(3m * 4n)
    # space O(m+n)