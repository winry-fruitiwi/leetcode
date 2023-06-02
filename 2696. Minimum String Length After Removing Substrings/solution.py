class Solution:
    # takes in a string of all uppercase letters and removes any instances
    # of the substrings "AB" or "CD", then returns the length.
    # When one of these substrings are found, the strings before and
    # after the substring join and may create a new substring.
    def minLength(self, s: str) -> int:
        # an index that we use to iterate over s
        i = 0
        
        # iterate over the string, but stop one index before it ends so
        # that we can subtract any substrings found
        while (i < len(s) - 1):
            # if the current character is A, check if the next one is B
            # if it is, remove the character and reset the iterator
                # is that possible?
            if s[i] == "A" and s[i+1] == "B":
                s = s[:i] + s[i+2:]
                i = 0
                continue
            
            # repeat, but with the first character being C and the second D
            if s[i] == "C" and s[i+1] == "D":
                s = s[:i] + s[i+2:]
                i = 0
                continue
            
            i += 1
        
        # return the length of the string
        
        return len(s)
    
