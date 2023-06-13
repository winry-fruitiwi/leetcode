class Solution:
    # Takes in an n by n binary matrix and returns the length of the
    # shortest path from the top-left corner to the bottom-right corner
    # using BFS. All visited cells have to be 0s and the adjacent cells
    # are connected diagonally as well as horizontally and vertically.
    # Directly traverses the grid without converting to nodes.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # if either the top-left corner or bottom-right corner are
        # not clear, that means it's impossible to find a clear path
        # between the two corners

        # create the queue that stores the next coordinates that I need to visit

        # a set of indices I've already visited

        # the number of times the outer loop has iterated, or the
        # number of cells visited. Starts at 1

        # while the queue exists:

            # measure the queue's length and iterate that many times

                # pop off the front of the queue and save the indices

                # if we're at the end, we can return the round number

                # check for zeroes in all 8 directions and add to queue if needed

            # increase the round number by 1

        return -1
