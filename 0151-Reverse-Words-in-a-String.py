# a method do not use built in function
class Solution(object):
    def reverseWords(self, s):
        arr = list(s)
        self.reverse_string(arr, 0, len(arr)-1)
        self.reverse_word(arr)
        word = self.trim_sides(arr)
        res = self.trim_space(word)
        return ''.join(res)


    def reverse_string(self, arr, l, r):
        '''reverse a given string'''
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1 ; r -= 1
        return arr
    
    
    def reverse_word(self, arr):
        '''reverse every words in a string'''
        l, r = 0 , 0
        while r < len(arr):
            while r < len(arr) and not arr[r].isspace(): r += 1
            self.reverse_string(arr, l, r-1)
            r += 1; l = r
        return arr
    
    def trim_sides(self, arr):
        '''str.strip() basically'''
        if ''.join(arr).isspace(): return []
        l , r = 0, len(arr) - 1
        while l < r and arr[l].isspace(): l += 1
        while l < r and arr[r].isspace(): r -= 1
        return arr[l:r+1]
    
    def trim_space(self, word):
        '''remove duplicating space in a word'''
        if not word: return []
        res = [word[0]]            
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace(): continue
            res.append(word[i])
        return res


# a method use it
def reverse_words(s):
    lst=s.split()
    index=0
    left,right=0,len(lst)-1
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
    return " ".join(lst)

# it would be too easy if use reverse