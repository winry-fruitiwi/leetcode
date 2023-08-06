class Solution:
    # Takes in an array of numbers and returns the length of the longest
    # alternating subarray, where an alternating subarray is a subarray
    # with its elements alternating between alternating[0] and alternating[0]+1.
    #
    # Note: The other thing I could do in the pseudocode is to keep a
    # list of all the current alternating subarrays
    # and check all of them while I'm iterating instead of
    # going back and forth between an alternating subarray and
    # finding other alternating subarrays. This might be more efficient
    def alternatingSubarray(self, nums: List[int]) -> int:
        # longest subarray length
        longestAlternating = -1
        
        # current subarray length
        currentSubLen = 0
        
        diff = 1
        
        # iterate through nums to the second-to-last element
        for i in range(len(nums) - 1):
            # print("i:", i)
            
            # retrieve the current and next elements
            current = nums[i]
            next = nums[i+1]
            
            # if the next element does not satisfy the condition for the new subarray:
            if next != current + diff:
                if longestAlternating < currentSubLen:
                    longestAlternating = currentSubLen
                
                currentSubLen = 0
                
                # print("no alternating sub:", current, next)
            
            # if there is not currently an alternating subarray:
            if currentSubLen == 0 and next == current + 1:
                currentSubLen = 2 # because there have been two elements already
                diff = -1
                
                # print("alternating sub found:", current, next)
            
            # now, if the next element is current + 1, then the list is still alternating
            elif next == current + diff:
                currentSubLen += 1
                diff *= -1
                # print("continuing alternating sub:", current, next)
            
            # at end of nums or alternation break, update longest subarray length
        
        if longestAlternating < currentSubLen:
            longestAlternating = currentSubLen
        
        if longestAlternating == 0:
            longestAlternating = -1
        
        # return the longest subarray length
        return longestAlternating
        
