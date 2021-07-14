# use a Trie to solve this problem
# https://blog.csdn.net/lisonglisonglisong/article/details/45584721
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        # remember this structure
        # https://stackoverflow.com/questions/62665603/what-does-use-of-trienode-data-structure-in-trienode-class-mean
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # add a child to TrieNode
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True # this node is a word

    def search(self, word: str) -> bool:
        # use dfs to search the solution
        node = self.root
        self.res = False # set default res
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isWord == True: # if find the word
                self.res = True
            return
        
        if word[0] == ".": # if counter .
            for n in node.children.values(): # for all nodes
                self.dfs(n, word[1:])
        else: # a character
            node = node.children.get(word[0]) # find it following node
            if not node: # if no word exist
                return 
            self.dfs(node, word[1:])
                    
# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/59725/Python-easy-to-follow-solution-using-Trie.
