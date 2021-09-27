#https://leetcode.com/discuss/interview-question/1346976/help-needed-number-of-ways-of-dividing-string-into-substrings-with-balanced-count-of-brackets

"""
A string that contains only the following => ‘(‘, ‘)’, ‘[’, ‘]’. At some places there is ‘?’ in place of any bracket.
Determine the number of WAYS OF DIVIDING THE STRING INTO TWO SUBSTRINGS so as to form two balanced substrings. Each substring can be formed by replacing all ‘?’s with appropriate bracket to make it a balanced substring.

Example:
S = [(?][??[
ans =2
it can be divided as

First point of dividing
s1 = [(?] -->[()]
s2=[??[ --> [()[
rearragned as ()[]

second point of dividing is
s1=[(?][?
s2-->?[
"""

import collections

a="(()())(()[][))(?)("

def findPair(a):
    res=0
    freq=collections.Counter(a)
    if abs(freq["("]-freq[")"])+abs(freq["["]-freq["]"])>freq["?"]:
        return None
    
    countRound,countSquare,countQuestion=0,0,0
    for c in a:
        if c=="(":
            countRound+=1
        elif c==")":
            countRound-=1
        elif c=="[":
            countSquare+=1
        elif c=="]":
            countSquare-=1
        elif c=="?":
            countQuestion+=1
        if abs(countRound) + abs(countSquare) <= countQuestion:
        # left is correct
            res+=1
        return res-1
findPair("(?][")