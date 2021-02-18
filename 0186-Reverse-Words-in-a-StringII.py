'''
Given an input string __ , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it  in-place  without allocating extra space?

'''

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
def reverseWords(s):

    """
    :type str: List[str]
    :rtype: void Do not return anything, modify str in-place instead.
    """    

    s.reverse()
    print(s)
    word = 0
    left, right = 0, 0
    while left <len(s):
        
        while word < len(s) and s[word] != " ":
            word += 1
        right = word -1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
        
        word += 1
        left = word
        
    print(s)
    
reverseWords(s)