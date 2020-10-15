# Oct 13, 2020
# Last Substring in Lexicographical Order

# find all 'last' letters in the str then take the max of all the substrs starting with the last letter
def lastSubstring(self, s: str) -> str:
    # map from chars to all indexes
    idxs = collections.defaultdict(list)
    for c in range(len(s)):
        idxs[s[c]].append(c) 
        
    last_char = max(idxs.keys())
    
    last_str = ' '
    for i in idxs[last_char]:
        cur_sub = s[i:]
        last_str = max(cur_sub, last_str)
    
    return last_str
        