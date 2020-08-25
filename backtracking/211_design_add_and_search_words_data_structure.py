# August 24, 2020
# Design a data structure that supports adding new words and finding if a string matches any previously added string. When
# searching for a word, '.' is used as a wildcard for any letter

# Node class:
# - each node has a list/map for letters
# - bool to mark whether it is the end of a word

# DFS/Trie:
# Add:
# - loop through the chars in the word and move to the matching list/map. If the Node, doesn't exist, create one.
# - Once you finish a word, mark the end bool as true

# Search (dfs):
# - Base case: if you reach the end of the word, return the current end bool
# - loop through the chars in the word and look for matching characters, return false when there is no match
# - if there is a period, try searching on any character
class Node():
    def __init__(self):
        self.letters = [-1]*26
        self.end = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for c in word:
            if curr.letters[ord(c)-ord('a')] == -1:
                curr.letters[ord(c)-ord('a')] = Node()
            curr = curr.letters[ord(c)-ord('a')]
        
        curr.end = True

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(self.root, word)


    def dfs(self, node, word):
        curr = node
        if len(word) == 0:
            return curr.end

        char = word[0]
        if char.isalpha():
            if curr.letters[ord(char)-ord('a')] == -1:
                return False
            return self.dfs(curr.letters[ord(char)-ord('a')], word[1:])
        
        for i in range(26):
            if curr.letters[i] != -1:
                if self.dfs(curr.letters[i], word[1:]):
                    return True
        return False