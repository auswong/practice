# Oct 11, 2020
# Maximum Number of Occurrences of a Substring

# find counts of all substrings with <= maxLetters unique characters
def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    # don't need to worry about maxSize bc if there is a substr with X occurences of length maxSize
    # there will be a substr with X occurences of length minSize
    occurences = collections.defaultdict(int)
    for start in range(len(s)-minSize+1):
        substr = s[start:start+minSize]
        if len(set(substr)) > maxLetters:
            continue
        occurences[substr] += 1
    if occurences:
        return max(occurences.values())
    return 0