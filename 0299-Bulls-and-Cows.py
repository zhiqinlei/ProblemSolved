'''
Easy, but interesting problem, because it can be solved in different ways.

Let us first evaluate number of bulls B: by definition it is number of places with the same digit in secret and guess: so let us just traverse our strings and count it.
Now, let us evaluate both number of cows and bulls: B_C: we need to count each digit in secret and in guess and choose the smallest of these two numbers. Evaluate sum for each digit.
Finally, number of cows will be B_C - B, so we just return return the answer!
Complexity: both time and space complexity is O(1). Imagine, that we have not 4 lengths, but n, then we have O(n) time complexity and O(10) space complexity to keep our counters.
'''


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        both = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        
        for j in set(guess):
            s, g = secret.count(j), guess.count(j)
            both += min(s,g)
        
        cow = both - bull
            
        return str(bull) + 'A' + str(cow) +'B'