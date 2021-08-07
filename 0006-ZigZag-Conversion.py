class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # trick one
        # https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
        if numRows ==  1 or numRows >len(s):
            return s
        
        idx ,step =0, 1# must have step, or res will be same as input
        res = [''] * numRows # if numRows = 3, res = ['','','']
        
        for ch in s:
            res[idx] += ch
            if idx == 0:# when reach the top row, go down
                step = 1
                
            elif idx == numRows -1: # when reach the bottom row, go up
                step = -1
                
            idx += step
            #@1 end  #
            # I like to explain the part above
            # take the str "PAYPALISHIRING" for example:
            # We start with variable index with the value 0, step with the value 1
            # Each row added with the next char
            # If we reach the bottommost row, we need to turn to the next above row, so we change the step value to -1
            # we keep the step value until we reach topmost row. DON'T CHANGE IT!
            # Again, if we reach the topmost row, we need to reset the step value to 1
            # What we need to remember is:
            # the zigzag pattern is just a pictorial image for us to have a better understanding
            # What the trick of algorithm is actually add the next char of the given string to different rows.
            # Don't really think how to move the cursor in the matrix.
            # It's really misleading way you think of this. Even it works, it's not efficient.
        
        return ''.join(res)
    # O(n) Time, O(n) Space
