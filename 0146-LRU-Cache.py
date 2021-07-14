class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict() # ordered Dict is composed by dic and double linkedlist
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic: 
            return -1
        value = self.dic.pop(key) # return the value of key and delete it
        self.dic[key] = value # set it back
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            if self.capacity >0: # in range
                self.capacity -= 1 
            else:
                self.dic.popitem(last = False) # popitem delete first or last, when last = true, LIFO, when last = False, FIFO follow to delete
        else:
            self.dic.pop(key) # if in it, delete and replace it
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Ordered Dict https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).

# Dict + double linkedlist https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList


