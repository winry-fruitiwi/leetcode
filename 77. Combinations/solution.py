class Solution:
    # a recursive algorithm that finds n choose k
    def combine(self, n: int, k: int) -> List[List[int]]:
        # recursive helper method. args: startRange, numChoices
        def createCombo(startRange, numChoices):
            # if there are zero choices left: return an empty partial combo in a list
            if numChoices == 0:
                return [[]]

            # results keeps track of all the combos found in the call
            results = []
    
            # iterate through all elements until I have enough numbers left to make the remaining choices with
            # since range is exclusive, bottom range is n-k+2 instead of n-k+1
            for i in range(startRange, n-numChoices+2):
                # use recursive call to get partial combos for a smaller k and smaller range of choices
                smallerCombos = createCombo(i + 1, numChoices - 1)

                # add new choice to each of the partial combos I got back from the recursive call
                for combos in smallerCombos:
                    combos.append(i)

                # add all combos to our results for this call
                results.extend(smallerCombos)

            # return results
            return results

        # return all of the combinations, made by createCombo
        return createCombo(1, k)
