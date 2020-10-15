# Oct 13, 2020
# Remove All Adjacent Duplicates in String 2:

# 1. push everything on a stack and keep track of the current duplicate count of the most recent char
#   a.if limit is reached, pop the duplicates and recalculate current duplicate count from the top
# 2. combine the stack chars at the end to get final result
def removeDuplicates(self, s: str, k: int) -> str:
    st = collections.deque()
    curr_count = 1
    for i in range(len(s)):
        if st and s[i] == st[-1]:           # stack has chars and next char equals prev char
            if curr_count == k-1:           # curr s char satisfies the removal condition
                for p in range(k-1):
                    st.pop()
                
                if st:
                    new_top = st[-1]        # adjusting curr_count based on top characters (if stack has chars)
                    curr_count = 1
                    while curr_count < len(st) and new_top == st[-1-curr_count]:
                        curr_count += 1                        
            else:                           # still forming possible duplicate string
                st.append(s[i])
                curr_count += 1
        else:                               # different char: append and reset count
            st.append(s[i])
            curr_count = 1
    
    return ''.join(st)