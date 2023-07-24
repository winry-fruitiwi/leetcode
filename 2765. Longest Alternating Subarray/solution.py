class Solution:
    # Takes in an array of numbers and returns the length of the longest
    # alternating subarray, where an alternating subarray is a subarray
    # with its elements alternating.
    #
    # Note: The other thing I could do in the pseudocode is to keep a
    # list of all the current alternating subarrays
    # and check all of them while I'm iterating instead of
    # going back and forth between an alternating subarray and
    # finding other alternating subarrays. This might be more efficient
    def alternatingSubarray(self, nums: List[int]) -> int:
        # longest subarray length
        
        # iterate through nums to the second-to-last element
        
            # if the next element is 1 greater than the previous one, start
            # keeping track of the current subarray length and iterate until
            # the end of the array
            
            # make sure that the array is alternating from there
            
            # at the end of the loop (end of nums or alternation is broken),
            # update longest subarray length
        
        # return the longest subarray length
        
