class Solution:
    # Takes in the string s and turns it into a palindrome
    # by replacing as few letters as possible. Breaks tie by
    # checking the lexicographical value of the current letter.
    # Returns the palindrome string.
    def makeSmallestPalindrome(self, s: str) -> str:
        # turn the string into a list for easier manipulation. This allows
        # for changing the string's indices directly and I believe it is more
        # memory efficient.
        s = list(s)
        
        # iterate through the string starting from 0 and ending at half the length (rounded down)
        # the reason why we're iterating to half the length is because we already
        # know what the other half of the characters we are iterating over are
        for i in range(int(len(s)/2)):
            # get the letter at i
            letter = s[i]
            
            # if it's not the same as the letter at -i, then compare ords
            # the letter with the greater ord becomes the letter with the smaller ord
            # however, to compare ords you can just see if the letter is greater or
            # less than the other
            if letter > s[-i-1]:
                s[i] = s[-i-1]
            elif letter < s[-i-1]:
                s[-i-1] = s[i]
        
        # return the new string in string form
        result = ""
        for e in s:
            result += e
        
        return result
