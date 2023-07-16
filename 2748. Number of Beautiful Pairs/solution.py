class Solution:
    # This takes in a list of ints and returns the number of beautiful pairs.
    # A beautiful pair is when the first digit of the first
    # num in the pair is coprime with the last digit of the second
    # num in the pair. Two nums are coprime if their gcd is 1.
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # the number of beautiful pairs
        beautifulPairs = 0
        
        # convert each int in the list to tuples of the first
        # and last digit to save conversion time
        for i in range(len(nums)):
            num = nums[i]
            numStr = str(num)
            nums[i] = (int(numStr[0]), int(numStr[-1]))
        
        # print(nums)
        
        # iterate to the second-to-last digit of nums
        for i in range(len(nums) - 1):
            num1Tuple = nums[i]
        
            # iterate from next element in nums to end of nums
            for j in range(i + 1, len(nums)):
                num2Tuple = nums[j]
                
                # print(num1Tuple, num2Tuple)
            
                # find the first char of the first digit
                num1 = num1Tuple[0]
                
                # find last char of second digit
                num2 = num2Tuple[1]
                
                # assume that the pair is coprime unless proven otherwise,
                # makes the code simpler
                beautifulPairs += 1
                
                # print("beautifulPairs before GCD:", beautifulPairs)
                
                # iterate backwards from 9 to 2
                for divisor in range(9, 1, -1):
                    # if both ints are divisible by this number, that
                    # means they are not coprime and the pair is not beautiful!
                    if num1 % divisor == 0 and num2 % divisor == 0:
                        beautifulPairs -= 1
                        # print("not coprime, beautifulPairs:", beautifulPairs)
                        break
        
        # return the number of beautiful pairs
        return beautifulPairs
        
