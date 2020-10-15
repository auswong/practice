# Oct 12, 2020
# Basic calculator: given a string expression, evaluate it

# Idea: use a stack, reverse the string, and
#   - append numbers (multi digit if necessary)
#   - simply append '+', '-', and ')' (opening parenthesis for a reversed str)
#   - evaluate the stack if you see '(' (closing parenthesis for a reversed str)
#   evaluate:
#       - perform an operation by popping 3 items and save result to external var
#       - repeat until stack is empty or you encounter a ')'
#       finally, reappend value to the stack
def evaluate (self, st):
    curr_val = st.pop() # must be numeric
    elem = curr_val
    while st and elem != ")":
        elem = st.pop()
        if elem == '+':
            curr_val += st.pop()
        elif elem == '-':
            curr_val -= st.pop()
    st.append(curr_val)
    return

def calculate(self, s: str) -> int:
    if not s:
        return 0
    st = collections.deque()
    s = s[::-1]
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            run = i+1
            while run < len(s) and s[run].isnumeric():
                run += 1
            temp = s[i:run]
            st.append(int(temp[::-1]))
            i = run
            continue
        elif s[i] == "+" or s[i] == "-" or s[i] == ")":
            st.append(s[i])
        elif s[i] == "(":
            self.evaluate(st) 
        i += 1
    self.evaluate(st)
    return st.pop()
