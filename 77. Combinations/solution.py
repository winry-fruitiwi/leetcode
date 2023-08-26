class Solution:
    # returns all permutations of nums, an array of distinct ints
    def permute(self, nums: List[int]) -> List[List[int]]:
        # create a list of results
        results = []

        # if there are no choices left to make, return an empty list with an empty choice
        if nums == []:
            return [[]]

        # iterate through every element of the list
        for i in range(len(nums)):
            num = nums[i]
            # make a call to this function, but without the current element
            copyOfNums = nums.copy()

            del copyOfNums[i]

            permutations = self.permute(copyOfNums)

            # append the current choice to all of the choices made and add it to the list of results
            for permutation in permutations:
                permutation.append(num)
            
            results.extend(permutations)

        # return results
        return results
