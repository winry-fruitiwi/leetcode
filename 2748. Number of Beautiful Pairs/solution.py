class Solution:
    # This takes in a list of nums and returns each beautiful pair,
    # where a beautiful pair is when the first digit of the first
    # num in the pair is coprime with the last digit of the second
    # num in the pair. Two nums are coprime if their gcd is no greater
    # than 1.
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # the number of beautiful pairs
        
        # convert each int in the list to strings to save
        # time from converting each int to a string inside the 
        # main loop
        
        # iterate to the second-to-last digit of nums
        
            # iterate through the next nums
            
                # find the first char of the first digit
                
                # find last char of second digit (convert both to int)
                
                # iterate backwards from 9 to 2
                
                    # if both ints are divisible by this number, that
                    # means they are not coprime!
                
                # if they are coprime, then the pair is beautiful and
                # the count of beautiful numbers should increase
        
        # return the number of beautiful pairs
        
