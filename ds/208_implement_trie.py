# May 14, 2020
# Trie (prefix tree):
# important note: need to distinguish when a node is the end of a word (leaf) or an inner node

# 1st version: used recursion to find nodes
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.leaf = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return None
        
        if word[0] not in self.children:
            create = Trie()
            
            if len(word) == 1:
                create.leaf = True
            
            self.children[word[0]] = create                
        else:
            if len(word) == 1:
                self.children[word[0]].leaf = True
        
        self.children[word[0]].insert(word[1:])
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return True
        
        if word[0] not in self.children:
            return False
        
        if len(word) == 1:
            if self.children[word[0]].leaf:
                return True
            return False
        
        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        
        if prefix[0] not in self.children:
            return False
        
        return self.children[prefix[0]].startsWith(prefix[1:])


# 2nd version: use for loop to iterate through dictionaries
# init and insert the same

def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return True
        
        search_dic = self.children
        for i in range(len(word)):
            if word[i] not in search_dic:
                return False
            
            if i == len(word)-1:
                if search_dic[word[i]].leaf:
                    return True
                return False
            
            search_dic = search_dic[word[i]].children
        

def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    if not prefix:
        return True
    
    search_dic = self.children
    for i in range(len(prefix)):
        if prefix[i] not in search_dic:
            return False

        search_dic = search_dic[prefix[i]].children
    
    return True